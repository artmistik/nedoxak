import viberbot
import os
import requests
import openai
from decouple import config

openai.api_key = config("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")
bot = viberbot.Api(auth_token=os.environ.get("50dbfaec35e7dc33-3df9882045e9a141-dba4ee1023d173f2"))

def handle_message(viber_request, response):
    user_message = viber_request.message.text

    generated_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    bot_response = generated_response.choices[0].text.strip()

    response.send(bot_response)

bot.set_message_handler(handle_message)

# Запускаем бота
bot.set_webhook(os.environ.get("VIBER_WEBHOOK_URL"))
