from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key = GROQ_API_KEY)

prompt = """You are a biology expert that is able to identify the strengths and weaknesses of a student. 
Use the following strengths and weaknesses to only return one list containing two dictionaries,one for strengths and one for weaknesses.
The dictionaries should contain two keys. Write a description of the student's strengths/weaknesses
for the description key, and give a list of the topics of the strengths/weaknesses for the topics key. 
Make sure the output string format can be parsed using json.loads, this is very important. Only return the list with the two dictionaries and nothing else.
Here are the strengths and weaknesses of the student:

strengths: {strengths}
weaknesses: {weaknesses}
"""

recommend = """Based on the given strengths and weaknesses of a student, give actionable inshits as to what the student can study in order
to score better in his upcoming examinations. Only output the reccomendations and nothing more.

strengths: {strengths}
weaknesses: {weaknesses}
"""