# CODE2040 Step Five API Challenge

import requests
import json
from _datetime import datetime
from datetime import timedelta


# API Token.
myAPIToken = '3624f3214a21f60da7488a0716e6eee3'

# POST request.
step5 = requests.post('http://challenge.code2040.org/api/dating', data={'token': myAPIToken} )

# Converts POST request to JSON and displays Response.
step5JSONResponse = json.loads(step5.text)
print(step5JSONResponse)

# Isolates Interval and Datestamp Keys and displays them.
interval = step5JSONResponse['interval']
datestamp = step5JSONResponse['datestamp']
print(interval)
print(datestamp)
print()

# Converts Datestamp string to Datetime Object and diplays Object.
dateStampObject = datetime.strptime(datestamp, '%Y-%m-%dT%XZ')
print(dateStampObject)

# Adds given Interval to Datestamp Object.
finalDateObject = dateStampObject + timedelta(seconds=interval)

# Converts Final Date Object to a String.
finalDateString = finalDateObject.strftime('%Y-%m-%dT%XZ')
print(type(finalDateString)) # test that conversion was done correctly

# Dictionary to POST.
dataToPost = {
    'token' : myAPIToken,
    'datestamp' : finalDateString
}

# API challenge Validation POST Request, Headers and Response.
step5Validate = requests.post('http://challenge.code2040.org/api/dating/validate', json=dataToPost)
print(step5Validate.request.headers)
print(step5Validate.text)


