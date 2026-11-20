from domain import risk_score, risk_band

def test_risk_bounds():
    assert risk_score(-1,-2,-3)==0
    assert risk_score(100,100,50)==100
    assert risk_score(5,2,1)==40

def test_bands():
    assert risk_band(69)=="Elevated"
    assert risk_band(70)=="Critical"
