from agents.symptom_agent import SymptomCheckerAgent

def test_analyze_symptoms():
    agent = SymptomCheckerAgent()
    result = agent.analyze_symptoms('fever, headache')
    assert result['status'] == 'success'
    assert any(item['symptom'] == 'fever' for item in result['triage'])
    assert any(item['symptom'] == 'headache' for item in result['triage'])
