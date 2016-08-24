import requests

# API access token
myToken = '3624f3214a21f60da7488a0716e6eee3'

# Code2040 API POST request for challenge info
step2 = requests.post('http://challenge.code2040.org/api/reverse', data={"token": myToken})
step2RequestResponse = step2.text
print(step2RequestResponse)

# Reverses API string using extended slices
step2RequestResponseReversed = step2RequestResponse[::-1]
print(step2RequestResponseReversed)
# Dictionary Created to send with POST request validation
step2dataToPost = {
    'string': step2RequestResponseReversed,
    'token': myToken
}
# Sends API POST request for challenge validation and displays text response
step2Validate = requests.post('http://challenge.code2040.org/api/reverse/validate', json=step2dataToPost)
print(step2Validate.text)
