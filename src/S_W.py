import pandas as pd
from log import logger
from prompt import prompt, llm    
import json
import os

#create logger
logger = logger("S_W")

#read data
try:
    questions = pd.read_json("./data/raw/quiz_data.json")['quiz']
    data = json.load(open("./data/raw/quiz_submission_data.json"))
    nested_data = {"data":data}
    response = pd.DataFrame(nested_data)["data"]
    logger.debug("Loaded the data")
except Exception as e:
    logger.error(f"error occurred: {e}")

#create sub data variables
try:
    quiz = questions[["title", "topic", "negative_marks", "correct_answer_marks", "questions_count", "max_mistake_count"]]
    questions = questions["questions"]
    user = response[["score", "accuracy", "final_score", "negative_score", "correct_answers", "incorrect_answers", "total_questions", "quiz"]]
    response = response["response_map"]
    logger.debug("formed quiz, questions, user, response")
except Exception as e:
    logger.error(f"error occurred: {e}")

#get strengths and weaknesses
strengths = []
weaknesses = []
at = 0

for item in response.items():
    for i in range(at, len(questions) - 1):
        if str(questions[i]["id"]) == item[0]:
            for j in questions[i]["options"]:
                if j["id"] == item[1]:
                    log_entry = {
                        "question": questions[i]["description"],  # Log the question
                        "explanation": questions[i]["detailed_solution"] # Log explanation
                    }
                    if j["is_correct"] == True:
                        strengths.append(log_entry)
                        at = i
                        continue
                    else:
                        weaknesses.append(log_entry)
                        at = i
                        continue


#pass data to llm to get description od strengths and weaknesses along with stong and weak topics
prompt = prompt.format(strengths = strengths, weaknesses = weaknesses)
result = llm.invoke(prompt).content

#separate strengths and weaknesses dictionaries given by the llm
try:
    data = json.loads(result)
    strengths = data[0]
    weaknesses = data[1]
    logger.debug("Obtained Strengths and Weaknesses")
except Exception as e:
    logger.error(f"Unexpected error: {e}")

#make interim directory in the data directory
data_path = "./data"
raw_data_path = os.path.join(data_path, 'interim')
os.makedirs(raw_data_path, exist_ok=True)

#save strengths
try:
    output_file = os.path.join(raw_data_path, "strengths.json")
    with open(output_file, "w") as file:
        json.dump(strengths, file, indent=4)
    
    logger.debug(f"Data written to {output_file}")
except Exception as e:
    logger.error(f"Error fetching data: {e}")

#save weaknesses
try:
    output_file = os.path.join(raw_data_path, "weaknesses.json")
    with open(output_file, "w") as file:
        json.dump(weaknesses, file, indent=4)
    
    logger.debug(f"Data written to {output_file}")
except Exception as e:
    logger.error(f"Error fetching data: {e}")

