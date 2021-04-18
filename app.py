import sched
import time
import requests
import mailsender

scheduler = sched.scheduler(time.time, time.sleep)


# function to check the website for available doodles
def check_crocket(sc):

    # getting crocket doodle available puppies web page
    r = requests.get('https://www.crockettdoodles.com/available-puppies')

    # getting text from the web page
    page_text = r.text

    # conditional statement to see if a text needs to be sent
    if page_text.find('none available at this time') == -1:
        # mailsender.send_bot_mail()
        # mailsender.send_bot_mail_admin()
        print("it does work??")
        exit(0)
    else:
        print("It doesnt work")

    scheduler.enter(30, 2, check_crocket, (sc, ))


check_crocket(scheduler)

def check_bot(sc):
    # send text to abhi to tell if bot is still running properly
    mailsender.is_running_text()

    # setting scheduler
    scheduler.enter(14400, 1, check_bot, (sc, ))


# scheduler to run script every certain number of seconds
scheduler.enter(30, 2, check_crocket, (scheduler, ))
scheduler.enter(14400, 1, check_bot, (scheduler, ))
scheduler.run()

