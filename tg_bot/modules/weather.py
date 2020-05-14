import pyowm
import json
import requests

from pyowm import timeutils, exceptions
from telegram import Message, Chat, Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import run_async

from tg_bot import dispatcher, updater, API_WEATHER
from tg_bot.modules.disable import DisableAbleCommandHandler


@run_async
def cuaca(update, context):
    args = context.args
    location = " ".join(args)
    if location.lower() == context.bot.first_name.lower():
        bot.sendMessage(update.effective_message, "Me still seen!")
        context.bot.send_sticker(update.effective_chat.id, BAN_STICKER)
        return

    try:
        owm = pyowm.OWM(API_WEATHER, language='en')
        observation = owm.weather_at_place(location)
        cuacanya = observation.get_weather()
        obs = owm.weather_at_place(location)
        lokasi = obs.get_location()
        lokasinya = lokasi.get_name()
        temperatur = cuacanya.get_temperature(unit='celsius')['temp']
        fc = owm.three_hours_forecast(location)

        # Simbol cuaca
        statusnya = ""
        cuacaskrg = cuacanya.get_weather_code()
        if cuacaskrg < 232: # Hujan badai
            statusnya += "⛈️ "
        elif cuacaskrg < 321: # Gerimis
            statusnya += "🌧️ "
        elif cuacaskrg < 504: # Hujan terang
            statusnya += "🌦️ "
        elif cuacaskrg < 531: # Hujan berawan
            statusnya += "⛈️ "
        elif cuacaskrg < 622: # Bersalju
            statusnya += "🌨️ "
        elif cuacaskrg < 781: # Atmosfer
            statusnya += "🌪️ "
        elif cuacaskrg < 800: # Cerah
            statusnya += "🌤️ "
        elif cuacaskrg < 801: # Sedikit berawan
            statusnya += "⛅️ "
        elif cuacaskrg < 804: # Berawan
            statusnya += "☁️ "
        statusnya += cuacanya._detailed_status
                    

        cuacabsk = besok.get_weather_code()

        bot.sendMessage(update.effective_message, "{} Weather today {}, is {}°C.\n").format(lokasinya,
                statusnya, temperatur)

    except pyowm.exceptions.api_call_error.APICallError:
        bot.sendMessage(update.effective_message, "Insert Location To gcufo")
    except pyowm.exceptions.api_response_error.NotFoundError:
    bot.sendMessage(update.effective_message, "Sorry,Location too gay to be founded 😞")
    else:
        return


__help__ = "weather_help"

__mod_name__ = "Weather"

CUACA_HANDLER = DisableAbleCommandHandler(["weather"], pass_args=True)
# ACCUWEATHER_HANDLER = DisableAbleCommandHandler("accuweather", accuweather, pass_args=True)


dispatcher.add_handler(CUACA_HANDLER)
# dispatcher.add_handler(ACCUWEATHER_HANDLER)
