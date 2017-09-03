from gtts import gTTS
import os
import weather, news, datetime, berryCurrency, googleCalendar

def main():
    message = createMessage()
    #message = "Suvi on tosi pieni hahaa suvi on helikopterikaakka! Sini on myos tosi pieni hahaaa ja stefan on paras"

    tts = gTTS(text=message, lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def createMessage():
    weatherString  = weather.getWeatherString()
    newsString     = news.getNewsString()
    calendarString = googleCalendar.getCalendarString()
    currencyString = berryCurrency.getCurrencyString()

    welcomeString = welcome()

    message = "{} How are you doing ma boy? {} {} {} {}. That is all for today. Berry out".format(welcomeString, weatherString, newsString, currencyString, calendarString)

    print(message)
    return message

def welcome():
    currentHour = datetime.datetime.now().hour
    # print(currentHour)
    if (12 < currentHour < 15):
        return "Good day Stefan."
    elif (15 < currentHour < 18):
        return "Good afternoon Stefan."
    elif (18 < currentHour < 00):
        return "Good evening Stefan."
    else:
        return "Good morning Stefan."


if __name__ == "__main__":
    main()
