# CODE2040 Step Five API Challenge

import requests
import json
from _datetime import datetime
from datetime import timedelta


# API Token
myToken = '3624f3214a21f60da7488a0716e6eee3'

# POST request
step5 = requests.post('http://challenge.code2040.org/api/dating', data={'token': myToken} )

# Converts POST request to JSON and displays response
step5JSONResponse = json.loads(step5.text)
print(step5JSONResponse)

# Isolates interval and datestamp keys and displays them
interval = step5JSONResponse['interval']
datestamp = step5JSONResponse['datestamp']
print(interval)
print(datestamp)
print()

# converts datestamp string to datetime object and diplays object
dateStampObject = datetime.strptime(datestamp, '%Y-%m-%dT%XZ')
print(dateStampObject)

# Adds given interval to datestamp object
finalDateObject = dateStampObject + timedelta(seconds=interval)

# Converts final date object to a string
finalDateString = finalDateObject.strftime('%Y-%m-%dT%XZ')
print(type(finalDateString)) # teste that conversion was done correctly

# Dictionary to POST
dataToPost = {
    'token' : myToken,
    'datestamp' : finalDateString
}

# API challenge validation POST request, headers and response
step5Validate = requests.post('http://challenge.code2040.org/api/dating/validate', json=dataToPost)
print(step5Validate.request.headers)
print(step5Validate.text)


