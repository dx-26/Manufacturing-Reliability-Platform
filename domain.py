def risk_score(age_years: float, downtime_hours: float, overdue_tasks: int) -> int:
    """Heuristic risk index (0-100), not a predictive failure probability."""
    return min(100, max(0, round(max(age_years,0)*3 + max(downtime_hours,0)*5 + max(overdue_tasks,0)*15)))

def risk_band(score: int) -> str:
    if score >= 70: return "Critical"
    if score >= 40: return "Elevated"
    return "Routine"
