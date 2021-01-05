import requests
from bs4 import BeautifulSoup
import re
import csv
# beautiful soup object and response from website
response = requests.get(r'https://www.freejobalert.com/punjab-government-jobs/')
soup = BeautifulSoup(response.content, 'lxml')

import smtplib, ssl
'''
port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
    # TODO: Send email here
'''
job  = []

get_detail_links = [] # link to post

with open(job_file.csv, 'w') as csvfile:
    #getting job details
    for text in soup.find_all('tr', attrs={"style":"border: 1px solid #000000;"}):
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(text.get_text())
    # TODO: getting link
    for link in soup.find_all('strong'):
        print(link.find('a').attrs['href'])