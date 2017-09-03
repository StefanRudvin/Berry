from gtts import gTTS
import os, berrySetup, datetime, argparse

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cur", help="enable Currency")
    parser.add_argument("--cal", help="enable Calendar")
    parser.add_argument("--w", help="Enable Weather")
    parser.add_argument("--n", help="Enable News")
    return parser.parse_args()

def main():
    args = parseArguments()

    message = createMessage(args)
    #message = "Suvi on tosi pieni hahaa suvi on helikopterikaakka! Sini on myos tosi pieni hahaaa ja stefan on paras"

    tts = gTTS(text=message, lang='en')
    tts.save("berry.mp3")
    os.system("mpg321 berry.mp3")


def createMessage(args):
    calendarString = bCalendar.getCalendarString() if args.cal else ""
    currencyString = bCurrency.getCurrencyString() if args.cur else ""
    weatherString  = bWeather.getWeatherString()   if args.w   else ""
    newsString     = bNews.getNewsString()         if args.n   else ""

    welcomeString = createWelcomeString()

    message = "{} How are you? {} {} {} {}. That is all for today. Berry out".format(welcomeString, weatherString, newsString, currencyString, calendarString)

    print(message)
    return message

def createWelcomeString():
    return welcome() + berrySetup.name + ". "

def welcome():
    currentHour = datetime.datetime.now().hour
    # print(currentHour)
    if (12 < currentHour < 15):
        return "Good day "
    elif (15 < currentHour < 18):
        return "Good afternoon "
    elif (18 < currentHour < 00):
        return "Good evening "
    else:
        return "Good morning "


if __name__ == "__main__":
    main()
