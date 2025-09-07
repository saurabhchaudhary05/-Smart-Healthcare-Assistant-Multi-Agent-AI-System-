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

from agents.knowledge_agent import MedicalKnowledgeAgent
from agents.lifestyle_agent import LifestyleCoachAgent
from agents.scheduler_agent import SchedulerAgent

class OrchestratorAgent:
    def __init__(self):
        self.knowledge_agent = MedicalKnowledgeAgent()
        self.lifestyle_agent = LifestyleCoachAgent()
        self.scheduler_agent = SchedulerAgent()

    def process_user_input(self, symptoms):
        # 1️⃣ Medical knowledge
        knowledge = self.knowledge_agent.fetch(symptoms)

        # 2️⃣ Lifestyle advice
        lifestyle = self.lifestyle_agent.provide_advice(symptoms)

        # 3️⃣ Set reminders
        reminders = self.scheduler_agent.set_reminders(lifestyle["lifestyle_advice"])

        # 4️⃣ Dummy triage (example logic)
        triage = []
        for s in symptoms:
            level = "low"
            if any(word in s.lower() for word in ["fever", "pain", "chest"]):
                level = "medium"
            triage.append({"symptom": s, "triage_level": level})

        return {
            "triage": triage,
            "knowledge": knowledge,
            "lifestyle": lifestyle,
            "reminders": reminders
        }
