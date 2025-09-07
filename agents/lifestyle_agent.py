# # Placeholder for Lifestyle Agent implementation
# class LifestyleCoachAgent:
#     def provide_advice(self, symptoms):
#         advice = []

#         for symptom in symptoms:
#             if symptom in ['fever', 'headache']:
#                 advice.append({'symptom': symptom, 'advice': 'Stay hydrated, rest well, and avoid stress.'})
#             elif symptom == 'chest pain':
#                 advice.append({'symptom': symptom, 'advice': 'Avoid physical exertion and consult a doctor immediately.'})
#             elif symptom == 'shortness of breath':
#                 advice.append({'symptom': symptom, 'advice': 'Avoid allergens, stay calm, and consult a healthcare provider.'})
#             else:
#                 advice.append({'symptom': symptom, 'advice': 'Maintain a healthy lifestyle and regular check-ups.'})

#         return {'lifestyle_advice': advice, 'status': 'success'}


from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class LifestyleCoachAgent:
    def __init__(self):
        self.llm = OpenAI(
            model_name="gpt-3.5-turbo",
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.5
        )
        self.prompt = PromptTemplate(
            input_variables=["symptom"],
            template="You are a lifestyle coach. Give actionable lifestyle advice for someone experiencing: {symptom}"
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def provide_advice(self, symptoms):
        advice_list = []
        for s in symptoms:
            advice = self.chain.invoke({"symptom": s})
            advice_list.append({"symptom": s, "advice": advice})
        return {"advice_list": advice_list}
