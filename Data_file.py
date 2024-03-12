# imports
import random
import praw
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from openpyxl import Workbook, load_workbook

# add your own reddit information
reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     user_agent = '')
# activating the workbook
workbook = Workbook()
worksheet = workbook.active
# subreddits that the code finds data for 
random_subreddit = ['ask','AskHistorians','NoStupidQuestions','AskScienceFiction','AskReddit','AskRedditAfterDark','Question','questions']
worksheet.append(['question','points','answers'])
# checks if it already found the data
dictionary = [['None',0,0]]
# add to dictionary
ii = 0
line = []
for row in worksheet:
    for cell in row:
        if cell.value == 'question' or cell.value == 'points' or cell.value == 'answers':
            pass
        else:
            line.append(cell.value)
    if len(line) > 0:
        dictionary.append(line)
        line = []
# ----------------------------
check = 0
# prediction
total_points = []
total_comments = []
for i in range(10):
    subreddit = reddit.subreddit(random.choice(random_subreddit))
    # for each post in the subreddit
    for post in subreddit.hot(limit = 10):
        # adds to dictionary
        for value in dictionary:
            if value[0] == post.title and value[1] == post.score:
                check = 0
            else:
                check = 1
        if check == 1:
            answers = 0
            for comment in post.comments:
                if hasattr(comment,"body"):
                    answers += 1
            # adds information about the data
            worksheet.append([str(post.title),int(post.score),int(answers)])
            total_points.append(post.score)
            total_comments.append(answers)
            dictionary.append([str(post.title),int(post.score),int(answers)])
    # saves the data
    workbook.save(r"C:\Users\danie\Desktop\New Microsoft Excel Worksheet.xlsx")
    print("save")
print("done")

# prediction
data = pd.read_excel(r"C:\Users\danie\Desktop\New Microsoft Excel Worksheet.xlsx")
x = data.drop(columns = ['question'])
y = data['question']
model = DecisionTreeClassifier()
model.fit(x,y)
prediction = model.predict([ [round(sum(total_points) / len(total_points)),round(sum(total_comments) / len(total_comments))] ])
print(prediction,'points {} answers {}'.format(round(sum(total_points) / len(total_points)),round(sum(total_comments) / len(total_comments))))
