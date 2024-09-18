import os
import openai

openai.api_key = "INSERT KEY"

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="write an email to my boss for resignation",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)
'''
{
  "id": "cmpl-8rkXxpBYFdkrpDN7vp5k68HTL76lu",
  "object": "text_completion",
  "created": 1707821001,
  "model": "gpt-3.5-turbo-instruct",
  "choices": [
    {
      "text": "\n\nSubject: Resignation Letter\n\nDear [Boss\u2019s Name],\n\nI am writing this email to inform you that I have decided to resign from my position at [company name]. It has been a pleasure working with such a dedicated and supportive team, and I am grateful for the opportunities and experiences that I have gained during my time here.\n\nI have carefully thought over my decision and have come to the conclusion that it is time for me to move on and explore new challenges and opportunities. I believe this decision will bring personal and professional growth for me.\n\nI will do my best to complete all my ongoing projects and ensure a smooth transition during my remaining time with the company. I am willing to assist in finding and training my replacement as well.\n\nI want to express my sincere gratitude to you for being an excellent boss and for all the support and guidance you have provided me throughout my tenure. I have learned a lot from you and will always be grateful for your mentorship.\n\nPlease let me know if there is any paperwork or formalities that need to be completed for my resignation. I will be happy to assist in any way possible.\n\nThank you for the wonderful experience and memories that I will cherish forever. I wish the company and my colleagues all the best for the future.\n\nSincerely",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 256,
    "total_tokens": 264
  }
}

'''