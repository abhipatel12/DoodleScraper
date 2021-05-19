
import smtplib, ssl


def send_bot_mail():

    # variables for emails
    sender_email = 'goldendoodle.bot@gmail.com'
    receiver_email = '7705700637@vtext.com'
    # receiver_email = '9122944497@txt.att.net'
    password = '*********'
    email_body = "\n\n\nThere's a pupper on the site. Go get it before someone else does!!! " \
                 "https://www.crockettdoodles.com/available-puppies "

    # setting port number
    port = 465

    # creating secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)

        # sending email
        server.sendmail(sender_email, receiver_email, email_body)


def send_bot_mail_admin():

    # variables for emails
    sender_email = 'goldendoodle.bot@gmail.com'
    receiver_email = '7705700637@vtext.com'
    password = '**********'
    email_body = "\n\n\nThere's a pupper on the site. Go get it before someone else does!!! " \
                 "https://www.crockettdoodles.com/available-puppies "

    # setting port number
    port = 465

    # creating secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)

        # sending email
        server.sendmail(sender_email, receiver_email, email_body)


# welcome text
def welcome_text():

    # variables for emails
    sender_email = 'goldendoodle.bot@gmail.com'
    receiver_email = '7705700637@vtext.com'
    # receiver_email = '9122944497@txt.att.net'
    password = '***********'
    email_body = 'Welcome to you goldendoodle bot. I will text you every time a dog shows up on Crocket doodle ' \
                 'page. There is no unsubscribing from this bot. '

    # setting port number
    port = 465

    # creating secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)

        # sending email
        server.sendmail(sender_email, receiver_email, email_body)


# text to see if bot is still running
def is_running_text():
    # variables for emails
    sender_email = 'goldendoodle.bot@gmail.com'
    receiver_email = '7705700637@vtext.com'
    # receiver_email = '9122944497@txt.att.net'
    password = '********'
    email_body = 'Your bot is still running somehow. '

    # setting port number
    port = 465

    # creating secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)

        # sending email
        server.sendmail(sender_email, receiver_email, email_body)


def gotcha():

    # variables for emails
    sender_email = 'goldendoodle.bot@gmail.com'
    receiver_email = '7708515777@vtext.com'
    # receiver_email = '9122944497@txt.att.net'
    password = '********'
    email_body = "\n\n\nThere's a pupper on the site... Lol nah jk  Goodnight :)"

    # setting port number
    port = 465

    # creating secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)

        # sending email
        server.sendmail(sender_email, receiver_email, email_body)