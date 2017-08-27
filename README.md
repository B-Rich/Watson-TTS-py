## Why should i use this instead of using the one on GitHub?
Well, this doesn't require the `watson_developer_cloud_service` module because it focuses on TTS.

# Stuff you need to be able to run this:
0. requests
1. urllib.parse

I think these are already installed, so yeah.

# How to install this?
Download the script for now. You will be able to install it with `pip` later.

# Usage:

### With auth()

```python
from watson import *
auth("username", "password")
link = parse("cool text huh")
get_file(link)
```

### Without auth()

`from watson_tts_py import *`
`link = parse("text that will be alive", "username", "password")`
`get_file(link)`

Done! The file should be saved as "output.wav"

# More stuff:

You can pass the audio type that you want and the voice that you want to the function `parse()` when calling it.
The default audio type is `.wav` and the default voice is `en-US_AllisonVoice`

And to change the file name, you can pass the name of your file to `get_file()` function when calling it.
Default file name is `output`


### An example:

```python
from watson_tts_py import *

url_link = parse("text", "username", "password", "ogg", "en-US_LisaVoice")
get_file(url_link, "TTS_output")
```

This will make a file called "TTS_output.ogg" that has what you want.


Here is an example of running the script with parameters which is the same.

### An example:
```python
from watson_tts_py import *

url_link = parse(text="text", username="username", password="password", audio_type="ogg", voice="en-US_LisaVoice")
get_file(url_link, file_name="TTS_output")
```

Also, i've added binary which returns the content of the file without writing to it.

### An example:
```python
from watson_tts_py import *
auth("username", "password")
x = parse("cool text", audio_type="ogg")
get_file(x, binary=True)
```

It will returns stuff you won't get but the output might be useful.
