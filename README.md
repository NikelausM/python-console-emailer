<p align="center"><img src="./images/logos/email-from-python-script.jpg" alt="Email From Python Logo." width=50%><p>

# Python Console Emailer

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Screenshots](#screenshots)
- [Launch](#launch)
- [Technologies](#technologies)

## Introduction
Python console emailer is a console (terminal) based python application that allows the user to sign in to their email and send emails to others using the email encryption type of their choice ([SSL](https://www.techopedia.com/definition/29747/secure-socket-layer-encryption-ssl-encryption) or [TLS](https://www.techopedia.com/definition/4143/transport-layer-security-tls)). The application allows the user to insert multiple text or html sections in the email via the command line (terminal).

The purpose of this mini-project was to gain a greater understanding of how emails are created, encrypted, and sent. Therefore, the application was developed with the [smtplib](https://docs.python.org/3/library/smtplib.html) python module to emulate some of the functionality of the [email](https://docs.python.org/3/library/email.message.html) python module.

## Features
- Choice of email encryption type ([SSL](https://www.techopedia.com/definition/29747/secure-socket-layer-encryption-ssl-encryption) or [TLS](https://www.techopedia.com/definition/4143/transport-layer-security-tls))
- Email sign-in
- Specify display name
  - User is able to change the display name that they would show up as in the inbox of the recipient (default is [email_username])
- Specify email subject
- Sending multi-part email
  - Able to create multiple text and/or html email body sections

## Screenshots

### Console Command Example
<img src="./images/screenshots/console_snapshot.PNG" alt="Screenshot of console user interface being used for the python console email application">

### Email in Recipient's Inbox
<img src="./images/screenshots/email_inbox_snapshot.PNG" alt="Screenshot of the email in the recipient's inbox">

### Email Message
<img src="./images/screenshots/email_snapshot.PNG" alt="Screenshot of the email when it has been opened">

## Launch
In the command line:
```
python emailer_smtp.py -e ssl
```
or,
```
python emailer_smtp.py -e tls
```
For help, enter:
```
python emailer_smtp.py -h
```
or,
```
python emailer_smtp.py --help
```

## Technologies
- [Python 3.8.3](https://www.python.org/downloads/release/python-383/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)
