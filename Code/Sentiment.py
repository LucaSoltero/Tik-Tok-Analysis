# Author: Luca Soltero
# Email: lsoltero@usc.edu
# Course: Introduction to Econometrics (ECON 318) USC

import Analysis
from time import sleep
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_Sentiment(caption):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Decide whether a TikTok's sentiment is positive, neutral, or negative.\n\nCaption: "
               f"\"{caption}\""
               "\nSentiment:",
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    print(response)
    sent = response["choices"][0]["text"].strip()
    if sent == "Positive":
        return "Positive"
    else:
        return "False"


df = Analysis.dataFrame()


def write_list_to_file(filename):
    with open(filename, 'w') as file:
        for item in df["text"]:
            file.write(get_Sentiment(str(item)) + ", " + str(item) + '\n')
            sleep(2)