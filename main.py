import os
import openai
import datetime
import win32com.client
import speech_recognition as sr
import webbrowser
"""from config import apikey"""


chatStr = ""


def chat(query, prompt):
    global chatStr
    openai.api_key = "INSERT OPENAI KEY"
    chatStr += f"User: {query}\n Bagley: "
    text = f"Openai response for Prompt: {prompt} \n ****************************\n\n"
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]

    except Exception as e:
        return "some error occured,sorry from Bagley"


def ai(prompt):
    openai.api_key = "Insert key"
    text = f"Openai response for Prompt: {prompt} \n ****************************\n\n"""

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(s):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(s)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said {query}")
            return query
        except Exception as e:
            return "Some error occurred, sorry from Bagley"


if __name__ == '__main__':
    say("hello i am Bagley your desktop Artificial Intelligence assistant")
    while True:
        print("listening...")
        query = takecommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} now....")
                webbrowser.open(site[1])
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strfTime}")
        elif "Using your AI".lower() in query.lower():
            ai(prompt=query)
        elif "Bagley that's all for now".lower() in query.lower():
            exit()
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        else:
            print("chatting....")
            chat(query, prompt=query)
