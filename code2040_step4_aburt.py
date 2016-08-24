# CODE2040 Step Four API Challenge
import requests
import json

# My API Token
myToken = '3624f3214a21f60da7488a0716e6eee3'

# API POST request and response
step4 = requests.post('http://challenge.code2040.org/api/prefix', data={'token': myToken})
print(step4.text)

# JSON decoder
step4jsonResponse = json.loads(step4.text)

# isolates prefix and array keys and displays prefix
queryPrefix = step4jsonResponse["prefix"]
arrayToSearch = step4jsonResponse["array"]
print(queryPrefix)
print()

# array to POST
notTheSamePrefixArray = []

# Searches through list and determines whether target query exists in list
for index in range(len(arrayToSearch)):
    if queryPrefix not in arrayToSearch[index]:
        notTheSamePrefixArray.append(arrayToSearch[index])  # adds strings that do not contain prefix to list

# Dictionary to POST
dataToPost = {
    'token': myToken,
    'array': notTheSamePrefixArray
}

# API Validation POST request, Request Headers, and response
step4Validate = requests.post("http://challenge.code2040.org/api/prefix/validate", json=dataToPost)
print(step4Validate.request.headers)
print(step4Validate.text)
