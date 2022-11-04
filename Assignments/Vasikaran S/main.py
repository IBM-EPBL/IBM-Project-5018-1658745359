from ibm_Watson import TextToSpeechV1
from ibm_Cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('xJkM8tB-t1x0gk7w8ufsDykw3kqdFMECmppf_00ZUMZp')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/f2849109-539b-4b9d-ab75-ceaa6da4b7e0')

with open('hello_world.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Hello world',
            voice='en-US_AllisonV3Voice',
            accept='audio/wav'
        ).get_result().content)
