---
# This top area is to give jekyll information about the page.
layout: default
permalink: /troubleshooting/openssl/
---

# Troubleshooting OPENSSL_1_1_1

We had some issues using Mary TTS:

```bash
[DEBUG:2020-10-31 08:09:28,178] rhasspyserver_hermes: Subscribed to hermes/tts/sayFinished
[DEBUG:2020-10-31 08:09:28,179] rhasspyserver_hermes: Subscribed to hermes/error/tts
[DEBUG:2020-10-31 08:09:28,180] rhasspyserver_hermes: Subscribed to hermes/audioServer/default/playBytes/#
[DEBUG:2020-10-31 08:09:28,180] rhasspyserver_hermes: Subscribed to hermes/error/audioServer/play
[DEBUG:2020-10-31 08:09:28,182] rhasspyserver_hermes: -> TtsSay(text='hallo', site_id='default', lang=None, id='60f6361d-5e7b-4d9f-aabd-dd10cf2cf838', session_id='')
[DEBUG:2020-10-31 08:09:28,184] rhasspyserver_hermes: Publishing 115 bytes(s) to hermes/tts/say
[DEBUG:2020-10-31 08:09:28,188] rhasspytts_cli_hermes: <- TtsSay(text='hallo', site_id='default', lang=None, id='60f6361d-5e7b-4d9f-aabd-dd10cf2cf838', session_id='')
[DEBUG:2020-10-31 08:09:28,190] rhasspytts_cli_hermes: ['bash', '-c', 'curl -sS -X GET -G --output - --data-urlencode INPUT_TYPE=TEXT --data-urlencode OUTPUT_TYPE=AUDIO --data-urlencode AUD                                                IO=WAVE --data-urlencode LOCALE=de --data-urlencode INPUT_TEXT="$0" http://localhost:5920/process', 'hallo']
curl: /usr/lib/rhasspy/rhasspy/libssl.so.1.1: version `OPENSSL_1_1_1' not found (required by /usr/lib/arm-linux-gnueabihf/libcurl.so.4)
[ERROR:2020-10-31 08:09:28,209] rhasspytts_cli_hermes: handle_say
Traceback (most recent call last):
  File "rhasspy-tts-cli-hermes/rhasspytts_cli_hermes/__init__.py", line 114, in handle_say
AssertionError: Non-zero exit code: 1
[DEBUG:2020-10-31 08:09:28,212] rhasspytts_cli_hermes: -> TtsError(error='Non-zero exit code: 1', site_id='default', context='60f6361d-5e7b-4d9f-aabd-dd10cf2cf838', session_id='')
[DEBUG:2020-10-31 08:09:28,212] rhasspytts_cli_hermes: Publishing 123 bytes(s) to hermes/error/tts
[DEBUG:2020-10-31 08:09:28,215] rhasspyserver_hermes: Handling TtsError (topic=hermes/error/tts, id=027266df-2553-4bdc-b935-cb4bd3a41a12)
[ERROR:2020-10-31 08:09:28,217] rhasspyserver_hermes: TtsError(error='Non-zero exit code: 1', site_id='default', context='60f6361d-5e7b-4d9f-aabd-dd10cf2cf838', session_id='')
[DEBUG:2020-10-31 08:09:28,218] rhasspytts_cli_hermes: -> TtsSayFinished(site_id='default', id='60f6361d-5e7b-4d9f-aabd-dd10cf2cf838', session_id='')
[DEBUG:2020-10-31 08:09:28,218] rhasspytts_cli_hermes: Publishing 84 bytes(s) to hermes/tts/sayFinished
[DEBUG:2020-10-31 08:09:28,222] rhasspydialogue_hermes: <- TtsSayFinished(site_id='default', id='60f6361d-5e7b-4d9f-aabd-dd10cf2cf838', session_id='')
[ERROR:2020-10-31 08:09:28,220] rhasspyserver_hermes: Non-zero exit code: 1
Traceback (most recent call last):
  File "quart/app.py", line 1821, in full_dispatch_request
  File "quart/app.py", line 1869, in dispatch_request
  File "rhasspy-server-hermes/rhasspyserver_hermes/__main__.py", line 1612, in api_text_to_speech
  File "rhasspy-server-hermes/rhasspyserver_hermes/__main__.py", line 1598, in speak
  File "rhasspy-server-hermes/rhasspyserver_hermes/__init__.py", line 596, in speak_sentence
rhasspyserver_hermes.TtsException: Non-zero exit code: 1
```

It seems that we do not have `'OPENSSL_1_1_1'` installed.  
So we tried to install v1.1.1:  
```
    wget https://www.openssl.org/source/openssl-1.1.1.tar.gz
    tar -zxf openssl-1.1.1.tar.gz && cd openssl-1.1.1
    ./config
    make
    make test
    make install
```

*We followed the official install [instructions](https://github.com/openssl/openssl/blob/OpenSSL_1_1_1/INSTALL).*  
Does not work.  

We tried to add the library-path: ``export LD_LIBRARY_PATH=/opt/openssl/lib:$LD_LIBRARY_PATH``  
Does not work.  
Not with alias not with other paths.  

We changed `/usr/lib/rhasspy/rhasspy/libssl.so.1.1` with `~/openssl-1.1.1/libssl.so.1.1`  
Does not work.  

`OPENSSL_1_1_1` is required by `/usr/lib/arm-linux-gnueabihf/libcurl.so.4` so we tried to reinstall this package.  
Does not work.  

We copied all files from `~/openssl-1.1.1` to `/usr/lib/rhasspy/rhasspy` and reinstalled it as root-user.  
That finally worked.