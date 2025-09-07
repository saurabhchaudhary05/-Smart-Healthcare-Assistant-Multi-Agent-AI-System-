# class SymptomCheckerAgent:
#     def __init__(self):
#         self.triage_rules = {
#             'fever': 'Monitor at home; drink fluids.',
#             'chest pain': 'Urgent: Consult a doctor immediately.',
#             'headache': 'Mild, rest and hydrate.',
#             'shortness of breath': 'Urgent: Seek medical attention now.'
#         }

#     def analyze_symptoms(self, user_input):
#         symptoms = user_input.lower().split(',')
#         recommendations = []

#         for symptom in symptoms:
#             symptom = symptom.strip()
#             advice = self.triage_rules.get(symptom, "General check-up recommended.")
#             recommendations.append({'symptom': symptom, 'advice': advice})

#         return {'triage': recommendations, 'status': 'success'}


class SymptomCheckerAgent:
    def analyze(self, symptoms):
        analysis = []
        for s in symptoms:
            triage_level = "low"
            if s.lower() in ["fever", "cough", "headache"]:
                triage_level = "medium"
            if s.lower() in ["chest pain", "difficulty breathing"]:
                triage_level = "high"
            analysis.append({"symptom": s, "triage": triage_level})
        return {"triage": analysis}

