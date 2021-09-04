# import flask related
from flask import Flask, request, abort
# import linebot related
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, AudioMessage,
    LocationSendMessage, ImageSendMessage, StickerSendMessage
)
from linebot.models.messages import FileMessage, ImageMessage
import goo
import datetime
now = datetime.datetime.now()
now_str = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
now_date = str(now.year) + ":" + str(now.month) + ":" + str(now.day)
now_dd = str(now.weekday())
if now_dd == "0":
    dd = "星期一"
elif now_dd == "1":
    dd = "星期二"
elif now_dd == "2":
    dd = "星期三" 
elif now_dd == "3":
    dd = "星期四"
elif now_dd == "4":
    dd = "星期五"
elif now_dd == "5":
    dd = "星期六"
elif now_dd == "6":
    dd = "星期日"
# create flask server
app = Flask(__name__)
# your linebot message API - Channel access token (from LINE Developer)
line_bot_api = LineBotApi('TUMeTx6e89YskIYfgtXw7azK/Qp7ghZ7zpG1ftadTfho9Ell85cnos4YHE/j2VYpkW8EcCtoo9Mo85iWp60zeaDWUqXFGulF/MHWb23P92wkQf0IZ3PZY/sz3rCxT/q3JSL1Ia6jcJxgW00XR08uNAdB04t89/1O/w1cDnyilFU=')
# your linebot message API - Channel secret
handler = WebhookHandler('2ab32fa9ab3cf313231d5348e012933f')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# handle msg
import os
import speech_recognition as sr

def transcribe(wav_path):
    '''
    Speech to Text by Google free API
    language: en-US, zh-TW
    '''
    
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio, language="zh-TW")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None
    
@handler.add(MessageEvent, message=AudioMessage)
def handle_audio(event):

    name_mp3 = 'recording.mp3'
    name_wav = 'recording.wav'
    message_content = line_bot_api.get_message_content(event.message.id)
    
    with open(name_mp3, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
    
    os.system('ffmpeg -y -i ' + name_mp3 + ' ' + name_wav + ' -loglevel quiet')
    text = transcribe(name_wav)
    print('Transcribe:', text)
    if text == "現在幾點":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=("現在時間"+now_str)))
    if text == "今天星期幾":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=(dd)))
    if text == "今天日期":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=("今天日期"+now_date)))

@handler.add(MessageEvent, message=FileMessage)
def handle(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    fileName = event.message.fileName.encode('utf-8')
    with open(fileName, 'wb',encoding='utf-8') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
        goo.goo(fileName)
# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)

