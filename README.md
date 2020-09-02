Introduction
============
This program can generate (by uploading as a private video to youtube and waiting for youtube's auto generated captions to do their magic) and hard code subtitles into videos.

Setup
============
* Required: Python 3.x
* Download dependencies from requirements.txt
```
pip install -r requirements.txt
```
* Set up FFmpeg. If Windows, download this [zip](https://ffmpeg.zeranoe.com/builds/) and follow this [article](https://www.wikihow.com/Install-FFmpeg-on-Windows) to set it up.
* Set up Youtube Data API Credentials.
  You'll see that there is no email/password options. Instead, the Youtube API uses [OAuth 2.0](https://developers.google.com/accounts/docs/OAuth2) to authenticate the upload. The first time you try to upload a video, you will be asked to follow a URL in your browser to get an authentication token. If you have multiple channels for the logged in user, you will also be asked to pick which one you want to upload the videos to. You can use multiple credentials, just use the option ```--credentials-file```. Also, check the [token expiration](https://developers.google.com/youtube/v3/) policies.

  The package used to include a default ```client_secrets.json``` file. It does not work anymore, Google has revoked it. So you now must [create and use your own OAuth 2.0 file](https://developers.google.com/youtube/registering_an_application), it's a free service. Steps:

  * Go to the Google [console](https://console.developers.google.com/).
  * _Create project_.
  * Side menu: _APIs & auth_ -> _APIs_
  * Top menu: _Enabled API(s)_: Enable all Youtube APIs.
  * Side menu: _APIs & auth_ -> _Credentials_.
  * _Create a Client ID_: Add credentials -> OAuth 2.0 Client ID -> Other -> Name: youtube-upload -> Create -> OK
  * _Download JSON_: Under the section "OAuth 2.0 client IDs". Save the file to your local system. 
  * Use this JSON as your credentials file: `--client-secrets=CLIENT_SECRETS` or copy it to `~/client_secrets.json`.

  *Note: ```client_secrets.json``` is a file you can download from the developer console, the credentials file is something auto generated after the first time the script is run and the google account sign in is followed, the file is stored at ```~/.youtube-upload-credentials.json```.*
