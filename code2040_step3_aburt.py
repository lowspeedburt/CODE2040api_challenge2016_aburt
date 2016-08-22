# CODE2040 Step Three Assessment Challenge
import requests
import json

# CODE2040 API Token.
myToken = '3624f3214a21f60da7488a0716e6eee3'

# POST request for challenge dictionary and response.
step3 = requests.post('http://challenge.code2040.org/api/haystack', data={'token': myToken})
print(step3.text)

# JSON module text to JSON decoding. Displays challenge dictionary.
step3jsonResponse = json.loads(step3.text)

# isolation of target String from API dictionary.
queryNeedle = step3jsonResponse["needle"]
print(queryNeedle)

# Returns index of the target String found in list.
foundNeedle = step3jsonResponse["haystack"].index(queryNeedle)
print(foundNeedle)

# Dictionary to POST for validation.
dataToPost = {
    'token': myToken,
    'needle': foundNeedle
}
# API Challenge Validation and response.
step3Validate = requests.post('http://challenge.code2040.org/api/haystack/validate', data=dataToPost)
print(step3Validate.text)
