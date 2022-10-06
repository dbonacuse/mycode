#!/usr/bin/env python3

""" Bonacuse Industries | Duncan 
        if, elif, else program """

message = 'As far as fall football weather goes, '

# wrap temp in float
temp = float(input("What is the temperature where you are? "))

# if input higher than 90

if temp >= 90:
    message = message + 'it is way too spicy for fall football.'
elif temp >= 70:
    message = message + 'you are getting there, but it is still a little toasty'
elif temp >= 50:
    message = message + 'congrats, these are some ideal conditions. You have now entered fall football season.'
elif temp >= 30:
    message = message + 'it is a little nippy for that perfect fall football, but this aint too bad'
else: 
    message = message + 'ooof. Layer up, kiddo.'
print(message)
