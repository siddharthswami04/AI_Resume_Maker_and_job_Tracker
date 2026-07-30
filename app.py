from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
import langchain
from langchain.agents import create_agent
from tavily import TavilyClient
import pytesseract as py
import streamlit as st
import os
import time
from PIL import Image
import pandas as pd
import numpy as np
TAVILY_API_KEY =" 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"
GROQ_API_KEY ="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"
GOOGLE_API_KEY ="AQ.Ab8RN6JWhO0L-Z8NKtu2EFVic-ZICA3a9fJjsGPi8QAhPf5Nzg"


model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash-lite',
    google_api_key=GOOGLE_API_KEY
)
# response = model.invoke("hello Buddy!")
# response.content[-1]['text']

def search_latest_news_jobs(query):
  '''This function helps to fetch latest
    news or jobs related article using tavily'''
  client=TavilyClient(
      api_key=TAVILY_API_KEY)
  response = client.search(query)
  return response


agent=create_agent(
    model=model,
    tools=[search_latest_news_jobs]

)
# agent

def main_agent(agent,query):
  '''this is main agent or leader agent orchestrate sub agent'''
  prompt='''you are ai assistance and below given is a prompt ,your task is to give detailed prompt for this.
  you are a professional resume generator where user will give their personal info you have to create detailed resume for students or professional one it must be with dynamic ui and ux ans,
  with advance css professional designing
  make sure to give output in html formnat only  no markdown allowed'''
  response = agent.invoke({'messages':[{'role':'user','content':prompt}]})
  detailed_prompt = response['messages'][-1].content[-1]['text']

  with open('prompt.txt','w') as f:
    f.write(detailed_prompt)
  return detailed_prompt

  user_details='''below given is a user details generate resume based on that
  if not given keep default resume python developer user details:{query}'''
  final_prompt=prompt+detailed_prompt+user_details
  response = agent.invoke({'messages':[{'role':'user','content':final_prompt}]})
  return response['messages'][-1].content[-1]['text']

  return code


# code = main_agent(agent,"ALAN TURING, GEN AI EXPERT")
# from IPython import display as DISPLAY
# DISPLAY.HTML(code)



def get_jobs(agent,location='delhi',profile='data analyst, SDE'):
  location='delhi'
  profile='data analyst, SDE'
  prompt="""Based on user given job proifile,using naukri,linkedin,indeed and other popular platform which are trusted and used to apply jobs
  ,so results with job profile name location salary company name requirements.
  show only jobs related to given{location}and{profile}
  output must be in professsional html naukri theme carts with dynamic design """
  response = agent.invoke({'messages':[{'role':'user','content':prompt}]})
  return response['messages'][-1].content[-1]['text']

  return code

# code = get_jobs(agent)
#  from IPython import display as DISPLAY
# DISPLAY.HTML(code)
