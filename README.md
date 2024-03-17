# RedditDataAnalyzer

This project uses Python and libraries like praw, pandas, sklearn, and openpyxl to analyze data from Reddit subreddits. It retrieves top posts, scores, and comments, and stores it in an Excel spreadsheet. A decision tree classifier from sklearn predicts post titles based on score and comments, demonstrating Python's ability to analyze social media data and understand post popularity and user engagement.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Imports](#Imports)
- [Rating: 5/10](#Rating)

# About

This project uses Python and libraries like praw, pandas, sklearn, and openpyxl to collect data from randomly selected subreddits on Reddit. It retrieves information about top posts, including title, score, and comments, and stores it in an Excel spreadsheet for analysis. A decision tree classifier from the sklearn library is used to predict the title of a post based on its score and comments. The classifier is trained on the collected data and used to predict the title of a new post. This project showcases how Python can be used to analyze data from social media platforms like Reddit, providing insights into post popularity and user engagement.

# Features

The project uses Python and various libraries to collect and analyze data from Reddit. It uses the praw library to retrieve information about top posts, including titles, scores, and comments. The collected data is organized and stored in an Excel spreadsheet, serving as a structured repository for further analysis. A decision tree classifier from the sklearn library is used to train the classifier on the collected data, learning patterns based on post scores and comments. The classifier predicts the title of a new post based on its score and comments, providing insights into the post's content. The project also provides insights into post popularity and user engagement, demonstrating how Python can be a powerful tool for extracting valuable insights from social media platforms like Reddit.

# Imports

random, Praw, panda, Sklearn.tree, openpyxl

# Rating

The code retrieves data from Reddit using PRAW, stores it in an Excel workbook, and performs a prediction using a Decision Tree classifier. It is modular, divided into sections for data retrieval, storage, and prediction. The code is suitable for fetching subreddit data using the Reddit API. However, there are several issues with the code, including incomplete Reddit information, hardcoded file paths, redundant data checking, repetitive saving, lack of error handling, and inefficient data representation.
To improve the code, users should provide clear instructions for Reddit API credentials, make file path handling configurable or use relative paths to ensure compatibility across different systems. Efficient data checking could be achieved by using a more efficient data structure or pandas DataFrame instead of iterating through each cell. Saving frequency should be optimized by saving the workbook only once after all data has been fetched from Reddit. Error handling should be implemented to handle potential exceptions gracefully and provide informative error messages to the user.\
Data storage optimization could involve exploring alternative options like SQLite databases or CSV files for better performance and scalability. Documentation and comments should be added to explain the purpose of each section of the code, making it easier for others to understand and modify. Overall, the code's shortcomings make it difficult for others to understand and modify.
