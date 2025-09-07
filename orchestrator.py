# from agents.symptom_agent import SymptomCheckerAgent
# from agents.knowledge_agent import MedicalKnowledgeAgent
# from agents.lifestyle_agent import LifestyleCoachAgent
# from agents.scheduler_agent import SchedulerAgent

# class OrchestratorAgent:
#     def __init__(self):
#         self.symptom_checker = SymptomCheckerAgent()
#         self.knowledge_agent = MedicalKnowledgeAgent()
#         self.lifestyle_agent = LifestyleCoachAgent()
#         self.scheduler_agent = SchedulerAgent()

#     def process_user_input(self, user_input):
#         # Step 1: Symptom Analysis
#         symptom_result = self.symptom_checker.analyze_symptoms(user_input)
#         symptoms_list = [item['symptom'] for item in symptom_result['triage']]

#         # Step 2: Medical Knowledge
#         knowledge_result = self.knowledge_agent.provide_knowledge(symptoms_list)

#         # Step 3: Lifestyle Advice
#         lifestyle_result = self.lifestyle_agent.provide_advice(symptoms_list)

#         # Step 4: Scheduler Agent sets reminders
#         reminders = []
#         for item in lifestyle_result['lifestyle_advice']:
#             reminder = self.scheduler_agent.schedule_reminder(item['symptom'], item['advice'])
#             reminders.append(reminder)

#         return {
#             'symptom_analysis': symptom_result,
#             'medical_knowledge': knowledge_result,
#             'lifestyle_advice': lifestyle_result,
#             'reminders': reminders
#         }

from agents.symptom_agent import SymptomCheckerAgent
from agents.knowledge_agent import MedicalKnowledgeAgent
from agents.lifestyle_agent import LifestyleCoachAgent
from agents.scheduler_agent import SchedulerAgent

class OrchestratorAgent:
    def __init__(self):
        self.symptom_checker = SymptomCheckerAgent()
        self.knowledge_agent = MedicalKnowledgeAgent()
        self.lifestyle_agent = LifestyleCoachAgent()
        self.scheduler_agent = SchedulerAgent()

    def process(self, symptoms):
        triage = self.symptom_checker.analyze(symptoms)
        knowledge = self.knowledge_agent.fetch(symptoms)
        lifestyle_advice = self.lifestyle_agent.provide_advice(symptoms)
        reminders = self.scheduler_agent.set_reminders(symptoms, lifestyle_advice["advice_list"])

        return {
            "symptom_analysis": triage,
            "medical_knowledge": knowledge,
            "lifestyle_advice": lifestyle_advice,
            "reminders": reminders
        }
