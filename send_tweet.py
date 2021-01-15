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

basic_tests_list = ["Min0", "Min1", "Append", "Pop", "Insert_front", "Insert_back", "Insert_random", "Length"]

# get most recent test times
if os.path.isfile('logs/.log_encoded.bin'):
    log_df = pd.read_csv('logs/.log_encoded.bin', encoding='IBM037')
    most_recent_tests = log_df.sort_values('test_date').drop_duplicates('test_name',keep='last')
    grading_tests = most_recent_tests[most_recent_tests['test_name'].isin(basic_tests_list)]
    passed_tests = grading_tests[grading_tests['passed_functionality_tests']]
    if passed_tests["elapsed_time"].count() == len(basic_tests_list):
        test_time_sum = passed_tests.sum()["elapsed_time"]

        # tweet it
        tweet = f'🏁 #queuerace update 🏁\n\n{os.environ["USERNAME"]} just pushed a queue that runs all the speed tests in {test_time_sum} seconds!\n\nCan you beat that? 🏎🏎🏎'
        auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_SECRET"])
        auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])
        api = tweepy.API(auth)
        api.update_status(tweet)

        # print(tweet)
