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
        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.llm = OpenAI(
            model_name="gpt-3.5-turbo",
            openai_api_key=openai_api_key,
            temperature=0.7
        )
        self.prompt = PromptTemplate(
            input_variables=["symptom"],
            template="You are a lifestyle coach. Give actionable lifestyle advice for someone experiencing: {symptom}"
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def provide_advice(self, symptoms):
        advice_list = []
        for s in symptoms:
            try:
                advice = self.chain.invoke({"symptom": s})
            except Exception as e:
                if "RateLimit" in str(e) or "quota" in str(e):
                    advice = "API quota exhausted or rate limit reached."
                else:
                    advice = f"Error: {str(e)}"
            advice_list.append({"symptom": s, "advice": advice})
        return {"lifestyle_advice": advice_list, "status": "success"}
