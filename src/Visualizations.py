from log import logger
import json
import pandas as pd
import matplotlib.pyplot as plt
import os

#create logger
logger = logger("Visualizations")

#load data
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

#make visualizations directory
os.makedirs("./visualizations", exist_ok=True)

#plot and save figure 1
names = ['Total', 'Attempted', 'Correct', 'Wrong']
values = [user["total_questions"], user["correct_answers"]+user["incorrect_answers"], user["correct_answers"], user["incorrect_answers"]]

title = 'Questions Analysis'
path = "./visualizations"
full_path = os.path.join(path, title)

plt.bar(names, values)
plt.title(title)
plt.xlabel('Questions')
plt.ylabel('Values')
plt.savefig(full_path)

logger.debug(f"saved figure: {title}")

#plot and save figure 2
names = ['Total', 'Achieved', 'Awarded', 'Decucted']
values = [user["total_questions"]*int(float(user["quiz"]["correct_answer_marks"])), int(float(user["final_score"])), user["score"], int(float(user["negative_score"]))]

title = 'Score Analysis'
path = "./visualizations"
full_path = os.path.join(path, title)

plt.bar(names, values)
plt.title(title)
plt.xlabel('Score')
plt.ylabel('Values')
plt.savefig(full_path)

logger.debug(f"saved figure: {title}")