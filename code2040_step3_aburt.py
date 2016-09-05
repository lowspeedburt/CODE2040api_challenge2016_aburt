# CODE2040 Step Three Assessment Challenge
import requests
import json

# CODE2040 API Token.
myAPIToken = '3624f3214a21f60da7488a0716e6eee3'

# CODE2040 Step 3 Challenge URL.
codeChallengeUrl = 'http://challenge.code2040.org/api/haystack'

# Validation URL for Step 3 challenge.
codeValidationUrl = 'http://challenge.code2040.org/api/haystack/validate'

# POST Request for challenge dictionary and Response.
step3 = requests.post(codeChallengeUrl, data={'token': myAPIToken})
print(step3.text)

# Converts POST Request to JSON.
step3jsonResponse = json.loads(step3.text)

# Isolation of target String from API dictionary.
queryNeedle = step3jsonResponse["needle"]
print(queryNeedle)

# Returns index of the target String found in List.
foundNeedle = step3jsonResponse["haystack"].index(queryNeedle)
print(foundNeedle)

# Dictionary to POST for Validation.
dataToPost = {
    'token': myAPIToken,
    'needle': foundNeedle
}
# API Challenge Validation and Response.
step3Validate = requests.post(codeValidationUrl, json=dataToPost)
print(step3Validate.text)
