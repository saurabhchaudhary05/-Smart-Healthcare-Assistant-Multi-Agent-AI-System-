# # Placeholder for Knowledge Agent implementation
# import json
# import os

# class MedicalKnowledgeAgent:
#     def __init__(self, knowledge_base_path='data/medical_knowledge.json'):
#         self.knowledge_base_path = knowledge_base_path
#         # Load knowledge base from JSON file
#         if os.path.exists(self.knowledge_base_path):
#             with open(self.knowledge_base_path, 'r') as file:
#                 self.knowledge_base = json.load(file)
#         else:
#             self.knowledge_base = {}

#     def provide_knowledge(self, symptoms):
#         knowledge = []
#         for symptom in symptoms:
#             info = self.knowledge_base.get(symptom, "No detailed information available.")
#             knowledge.append({'symptom': symptom, 'info': info})

#         return {'knowledge': knowledge, 'status': 'success'}

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class MedicalKnowledgeAgent:
    def __init__(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables. Check your .env file.")

        self.llm = OpenAI(
            model_name="gpt-3.5-turbo",
            openai_api_key=openai_api_key,
            temperature=0.5
        )
        self.prompt = PromptTemplate(
            input_variables=["symptom"],
            template="You are a helpful healthcare assistant. Explain in simple words the medical information about: {symptom}"
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def fetch(self, symptoms):
        knowledge = []
        for s in symptoms:
            try:
                info = self.chain.invoke({"symptom": s})
            except Exception as e:
                if "RateLimit" in str(e) or "quota" in str(e):
                    info = "API quota exhausted or rate limit reached."
                else:
                    info = f"Error: {str(e)}"
            knowledge.append({"symptom": s, "info": info})
        return {"knowledge": knowledge, "status": "success"}

