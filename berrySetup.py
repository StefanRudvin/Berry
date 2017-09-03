import sys

#
# Berry: raspberry pi wake up script setup
#

#
# These values can be changed after setup too.
#
name            = 'Stefan'
currencyBoolean = True
calendarBoolean = True
weatherBoolean  = True
newsBoolean     = True

berryWeatherLocation = "Espoo, fi"
berryWeatherTempUnit = 'celsius'


def main():
    print('******************************************')
    print('***************   BERRY   ****************')
    print('******************************************')

    print('Welcome to wakeMe, the python script.')

    print('*')
    print('What shall I call you?')
    name = raw_input()
    print('Very well {}. Now we shall set up components.'.format(berryName))

    print('******************************************')

    print('******************************************')

    print('Finished! All you need to do is name \'api_keys_example.py\' to \'api_keys.py\' and populate the keys.')


def setBooleans():
    currencyBoolean = query_yes_no("Include currency?")
    print('*')
    weatherBoolean = query_yes_no("Include weather?")
    print('*')
    newsBoolean = query_yes_no("Include news?")
    print('*')
    calendarBoolean = query_yes_no("Include google calendar?")

    if calendarBoolean:
        calendarUrl = 'https://developers.google.com/google-apps/calendar/quickstart/python'
        print('Run follow instructions on {} and run googleCalendarSetup.py to implement google calendar'.format(calendarUrl))

#
# query_yes_no http://code.activestate.com/recipes/577058/
#

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")






if __name__ == "__main__":
    main()
