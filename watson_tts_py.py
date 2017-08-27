import requests
from urllib.parse import urlencode
__author__ = "@dizaztor"

x_audio_type = None


def parse(username, password, text, audio_type=None, voice=None):
    query = urlencode([
        ("text", text)])
    if audio_type is not None:
        global x_audio_type
        x_audio_type = "{}".format(audio_type)
        audio_type = audio_type

    elif audio_type is None:
        audio_type = "wav"
        x_audio_type = "wav"

    else:
        pass

    if voice is not None:
        voice = voice

    elif voice is None:
        voice = "en-US_AllisonVoice"

    else:
        pass

    data = "https://{}:{}@stream.watsonplatform.net/text-to-speech/api/v1/synthesize?accept=audio/{}&{}&voice={}".format(username, password, audio_type, query, voice)
    return(data)


global URL_LINK
URL_LINK = None


def get_file(URL_LINK, file_name=None):

    if file_name is not None:
        file_name = "{}".format(file_name) + ".{}".format(x_audio_type)

    elif file_name is None:
        file_name = "output" + ".{}".format(x_audio_type)

    else:
        pass

    if URL_LINK is None:
        return "Please type in your username, password and your text."

    else:
        try:
            file = requests.get(URL_LINK)
            TTS = file.content

            with open(file_name, "wb") as output:
                output.write(TTS)

        except:
            return("Couldn't complete the job.")
