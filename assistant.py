import subprocess
import os
from groq import Groq
from PIL import ImageGrab
from dotenv import load_dotenv

load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def groq_prompt(prompt):
  convo = [{'role': 'user', 'content': prompt}]
  chat_completion = groq_client.chat.completions.create(messages=convo, model="llama3-8b-8192")
  response = chat_completion.choices[0].message

  return response.content

def function_call(prompt):
  sys_msg = (
    'You are an AI function calling model. You will determine whether extracting the users clipboard content, '
    'taking a screenshot, capturing the webcam or calling no functions is best for voice assistant to respond '
    'to the users prompt. The webcam can be assumed to be normal laptop webcam facing the user. You will '
    'respond with only one selection from this list: ["extract clipboard", "take screenshot", "capture webcam", "None"] \n'
    'Do not respond with anything but the most logical selection from that list with no explanations. Format the '
    'function call name exactly as I listed.'
  )
  function_convo = [{'role': 'system', 'content': sys_msg},{'role': 'user', 'content': prompt}]

  chat_completion = groq_client.chat.completions.create(messages=function_convo, model="llama3-8b-8192")
  response = chat_completion.choices[0].message

  return response.content

def take_screenshot():
  path = 'screenshot.jpg'
  screenshot = ImageGrab.grab()
  rgb_screenshot = screenshot.convert("RGB")
  rgb_screenshot.save(path, quality=15)

def web_cam_capture():
  return None

def get_clipboard_text():
  return None

prompt = input('USER: ')
response = groq_prompt(prompt)
function_response = function_call(prompt)
print("Function call: ", function_response)
print(response)