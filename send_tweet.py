# send_tweet.py
# by Jacob Wolf
# 
# Script to post a tweet with statistics about a student's most recent queue
# performance based on the logs. To be called by a Github action which sets environment
# variables for the API secrets
# 
# =============================================================================
#  More-Than-You-Need-To-Know Lounge
# =============================================================================
# Welcome to the More-Than-You-Need-To-Know Lounge, a chill place for code that
# you don't need to understand.

# Thanks for stopping by, we hope you find something that catches your eye.
# But don't worry if this stuff doesn't make sense yet -- as long as we know
# how to use code, we don't have to understand everything about it.

# Of course, if you really like this place, stay a while. You can ask a
# teacher about it if you're interested.
#
# =============================================================================

import tweepy
import os
import pandas as pd

#basic_tests_list = ["Min0", "Min1", "Append", "Pop", "Insert_front", "Insert_back", "Insert_random", "Length"]

basic_tests_list = ["Append","Pop","Insert_random","Length"]

# get most recent test times
if os.path.isfile('logs/.log_encoded.bin'):
    log_df = pd.read_csv('logs/.log_encoded.bin', encoding='IBM037')
    student_df = log_df[log_df["struct_name"]=="StudentQueue"]
    deque_df = log_df[log_df["struct_name"]=="Python deque"]
    most_recent_student = student_df.sort_values('test_date').drop_duplicates('test_name',keep='last')
    most_recent_deque = deque_df.sort_values('test_date').drop_duplicates('test_name',keep='last')
    student_grading_tests = most_recent_student[most_recent_student['test_name'].isin(basic_tests_list)]
    deque_grading_tests = most_recent_deque[most_recent_deque['test_name'].isin(basic_tests_list)]
    deque_grading_tests = deque_grading_tests.set_index("test_name")
    student_passed_tests = student_grading_tests[student_grading_tests['passed_functionality_tests']]
    if student_passed_tests["elapsed_time"].count() == len(basic_tests_list):
        # tweet it
        # tweet = f'🏁 #queuerace update 🏁\n\nUSERNAME just pushed a queue!'
        tweet = f'🏁 #queuerace update 🏁\n\n{os.environ["USERNAME"]} just pushed a queue with the following stats:'
        tweet += f'\n\nThroughput (relative to performance target):\n'
        sum_deque_times = sum(deque_grading_tests["elapsed_time"])
        weighted_throughputs_list = []
        for index, test in student_passed_tests.iterrows():
            deque_test_time = deque_grading_tests.loc[test["test_name"]]["elapsed_time"]
            throughput = 100*deque_test_time / test["elapsed_time"]
            tweet += f'|   {test["test_name"]}: {round(throughput, 2)}%\n'
            test_weight = (1/40) + (9/10)*(deque_test_time/sum_deque_times)
            weighted_throughputs_list.append(throughput*test_weight)
        throughput_score = sum(weighted_throughputs_list)
        tweet += f'Score: {round(throughput_score*10, 2)}'
        tweet += "\n\nCan you beat that? 🏎🏎🏎"
        auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_SECRET"])
        auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])
        api = tweepy.API(auth)
        api.update_status(tweet)

        # print(tweet)
