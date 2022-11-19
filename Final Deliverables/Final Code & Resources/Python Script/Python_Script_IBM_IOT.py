import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#Providing IBM Watson Device Credentials
organization = "jzl1k0"
deviceType = "PASWASR"
deviceId = "PASWASR"
authMethod = "token"
authToken = "ebilacranibav"




authenticator = IAMAuthenticator('ybW5L7XKtrYn47GWjKNo2vG3teltpl9bc6LeHh0bV2S3')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/98528c16-2a4f-414e-ba24-64d3472d69d8')

with open('PASWASR.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Its Time To Take The Medicine:"{f.user input(Enter medicine name)},{f.user input(Time),{f.user input(Date}}
            voice='en-US_AllisonV3Voice',
            accept='audio/wav'        
        ).get_result().content)
