#!/usr/bin/env python3

# Importing Libraries
import os
import csv
import time
import instaloader

print('Enter your account name:')
username = input()
print('Enter your account password:')
password = input()

# get the start time
st = time.time()

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
bot.login(user=username, passwd=password)

print("Login successfull!")

# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, username)
followers = set(f.username for f in profile.get_followers())
print("Number followers currently =>", profile.followers)

# check with previous file only if exist
if os.path.isfile(username+'.csv'):
    # read previous file
    previous_file = open(username+'.csv')
    csvreader = csv.reader(previous_file)
    previous_followers = set()
    for [row] in csvreader:
        previous_followers.add(row)
    print("Number followers previously =>", len(previous_followers))

    # open the file in the write mode
    f = open(username+'.csv', 'w', encoding='UTF8', newline='')

    print("Followers losts", [
          x for x in followers if x not in previous_followers])
    print("Followers wins", [
          x for x in previous_followers if x not in followers])

for follower in followers:
    # create the csv writer
    writer = csv.writer(f)
    writer.writerow([follower])

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
