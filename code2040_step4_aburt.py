# CODE2040 Step Four API Challenge
import requests
import json

# My API Token
myAPIToken = '3624f3214a21f60da7488a0716e6eee3'

# API POST Request and Response
step4 = requests.post('http://challenge.code2040.org/api/prefix', data={'token': myAPIToken})
print(step4.text)

# Converts POST Request to JSON.
step4jsonResponse = json.loads(step4.text)

# Isolates Prefix and Array Keys and displays Prefix
queryPrefix = step4jsonResponse["prefix"]
arrayToSearch = step4jsonResponse["array"]
print(queryPrefix)
print()

# Array Collection that will hold all strings that do not contain the target Prefix.
notTheSamePrefixArray = []

# Searches through Array Collection and determines whether Target Prefix exists.
for index in range(len(arrayToSearch)):
    if queryPrefix not in arrayToSearch[index]:
        notTheSamePrefixArray.append(arrayToSearch[index])  # adds strings that do not contain prefix to list

# Dictionary to POST
dataToPost = {
    'token': myAPIToken,
    'array': notTheSamePrefixArray
}

# API Validation POST Request, Request Headers, and Response
step4Validate = requests.post("http://challenge.code2040.org/api/prefix/validate", json=dataToPost)
print(step4Validate.request.headers)
print(step4Validate.text)
