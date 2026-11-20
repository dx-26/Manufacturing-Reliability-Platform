import pandas as pd
import streamlit as st
from domain import risk_score, risk_band
from storage import initialize, query, execute

st.set_page_config(page_title="Reliability Platform",page_icon="🏭",layout="wide")
initialize("""
CREATE TABLE IF NOT EXISTS assets(id INTEGER PRIMARY KEY,name TEXT NOT NULL,area TEXT NOT NULL,age_years REAL NOT NULL,downtime_hours REAL NOT NULL,overdue_tasks INTEGER NOT NULL DEFAULT 0);
CREATE TABLE IF NOT EXISTS work_orders(id INTEGER PRIMARY KEY,asset_id INTEGER NOT NULL,summary TEXT NOT NULL,priority TEXT NOT NULL,status TEXT NOT NULL DEFAULT 'Open',created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY(asset_id) REFERENCES assets(id));
""","""
INSERT INTO assets(name,area,age_years,downtime_hours,overdue_tasks) VALUES
('Line A Wrapper','Packaging',8,7,2),('Conveyor B','Assembly',4,3,0),('Press C','Production',12,9,3);
INSERT INTO work_orders(asset_id,summary,priority,status) VALUES (3,'Inspect vibration and lubrication','Critical','Open');
""")
st.title("🏭 Manufacturing Reliability Platform")
st.caption("Operational risk heuristics • sample data • not a certified safety system")
a,b,c=st.tabs(["Asset risk","Add asset","Maintenance work orders"])
with a:
    assets=query("SELECT * FROM assets ORDER BY id")
    ranked=[{**x,'risk_index':risk_score(x['age_years'],x['downtime_hours'],x['overdue_tasks']),'risk_band':risk_band(risk_score(x['age_years'],x['downtime_hours'],x['overdue_tasks']))} for x in assets]
    st.dataframe(pd.DataFrame(ranked),hide_index=True,use_container_width=True)
    if ranked:
        st.metric("Critical assets",sum(x['risk_band']=='Critical' for x in ranked))
        st.bar_chart(pd.DataFrame(ranked).set_index('name')['risk_index'])
    st.download_button("Export asset risk",pd.DataFrame(ranked).to_csv(index=False),"asset_risk.csv","text/csv")
    st.caption("Risk index = 3 × age in years + 5 × downtime hours + 15 × overdue tasks, capped at 100. Calibrate before operational use.")
with b:
    with st.form("new_asset"):
        name=st.text_input("Equipment name")
        area=st.text_input("Work area")
        age=st.number_input("Age (years)",min_value=0.0,value=2.0)
        downtime=st.number_input("Downtime in review window (hours)",min_value=0.0,value=0.0)
        overdue=st.number_input("Overdue tasks",min_value=0,value=0,step=1)
        if st.form_submit_button("Add asset"):
            if name.strip() and area.strip():
                execute("INSERT INTO assets(name,area,age_years,downtime_hours,overdue_tasks) VALUES (?,?,?,?,?)",(name.strip(),area.strip(),age,downtime,overdue))
                st.success("Asset added")
            else: st.error("Name and area are required")
with c:
    assets=query("SELECT id,name FROM assets ORDER BY name")
    options={f"{x['id']}: {x['name']}":x['id'] for x in assets}
    with st.form("work"):
        sel=st.selectbox("Asset",list(options))
        task=st.text_input("Maintenance summary")
        priority=st.selectbox("Priority",["Routine","Elevated","Critical"])
        if st.form_submit_button("Create work order"):
            if task.strip():
                execute("INSERT INTO work_orders(asset_id,summary,priority) VALUES (?,?,?)",(options[sel],task.strip(),priority))
                st.success("Work order created")
            else: st.error("Enter a task")
    orders=query("SELECT w.id,a.name AS asset,w.summary,w.priority,w.status,w.created_at FROM work_orders w JOIN assets a ON a.id=w.asset_id ORDER BY w.id DESC")
    st.dataframe(pd.DataFrame(orders),hide_index=True,use_container_width=True)
    open_orders=[x for x in orders if x['status']=='Open']
    if open_orders:
        selected_order=st.selectbox("Close an open work order",[f"{x['id']}: {x['summary']}" for x in open_orders])
        if st.button("Mark completed"):
            execute("UPDATE work_orders SET status='Completed' WHERE id=?",(int(selected_order.split(':')[0]),))
            st.rerun()
