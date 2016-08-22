# CODE2040 Step 1 Authentication for Technical Assessment Challenge##
import requests

# API Token
myToken = '3624f3214a21f60da7488a0716e6eee3'

# Dictionary to POST for authentication
dataToPost = {
    'github': 'https://github.com/skinnyal/CODE2040api_challenge2016_aburt',
    'token': myToken
}

# API POST request and response
step1 = requests.post('http://challenge.code2040.org/api/register', data=dataToPost)
print(step1.text)
