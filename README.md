# Berry
Berry wakes you up with news, calendar events, weather and currency information.
Then it speaks it to you using google's text to speech implementation.
Ideal for use with a raspberry pi.


Sample response:

> Good morning Stefan. What's up?

> Today is going to be a wicked day with the current temperature at 9 degrees, humidity at 76 percent and windspeed at 6 meters per second.

> Here are the latest titles from BBC News:

> Hurricane Harvey: Texas governor warns bill could be $180bn.
> Frankfurt WW2 bomb defused after mass evacuation.
> Cambodia Daily newspaper closes in government tax row.
> That is all for the news for today. 

> The GBP to EURO currency rate is 1.079.

> You have 1 event coming up today. Boxing starts at 09.

> That is all for today. Berry out


## Setup

* sudo apt-get install pip

* pip install -r requirements.txt

* Rename **api_keys_example.py** to **api_keys.py**

  * Populate API keys from https://newsapi.org/ and https://openweathermap.org/api

* **python googleCalendarSetup.py** if you wish to use google calendar

  * https://developers.google.com/google-apps/calendar/quickstart/python
  
* run main.py with desired arguments

## Arguments (Atleast 1 required)

* --cur Currency
* --cal Calendar
* --w Weather
* --n News
