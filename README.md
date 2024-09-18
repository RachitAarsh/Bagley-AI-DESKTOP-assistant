# Bagley-AI-DESKTOP-assistant

Project Overview
Bagley is an AI-powered desktop assistant built with OpenAI's GPT model. It listens to user commands via speech, responds via voice, and can interact with websites, provide current time, and more. It saves conversations in text files and can process additional prompts based on OpenAI’s API.


Key Features:- 

Voice Interaction: Bagley listens to your voice commands using the speech_recognition library.
AI Responses: Uses OpenAI’s GPT-3.5 to generate intelligent responses to queries.
Voice Output: Bagley speaks its responses through the system’s speakers using win32com.client.
Web Interaction: Opens popular websites like YouTube, Wikipedia, and Google via voice command.
Customizable Prompts: You can provide custom prompts to the OpenAI model for tailored responses.
Conversation Log: Saves conversations to text files in the Openai/ directory.


Setup and Installation:-

Clone the Repository:
git clone https://github.com/your-username/bagley-ai-assistant.git
cd bagley-ai-assistant
Install Dependencies: Make sure you have the required libraries installed by running:
pip install openai speechrecognition pywin32
Add Your OpenAI API Key: Replace INSERT OPENAI KEY with your actual API key inside the code.
Run the Program: Simply run the script to start Bagley:
python main.py


Usage:-

Bagley will start listening for your voice commands once launched.
It can respond to common tasks like opening websites, telling the current time, or chatting based on AI responses.
To stop the conversation, you can say "Bagley that's all for now".
Reset the chat history by saying "Reset chat".


Custom Prompts:- 

You can customize how Bagley responds by giving it specific prompts:
To use AI for generating responses, say "Using your AI" followed by the desired prompt.
The conversation history is saved in text files under the Openai/ directory.


Future Improvements:-

Add more website integrations.
Enable dynamic API key input via environment variables or config file.
Add GUI for more user-friendly interaction.


Contributing:-

Feel free to fork the project and make your improvements. Contributions are welcome!

