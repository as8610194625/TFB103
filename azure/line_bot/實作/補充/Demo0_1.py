from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, AudioSendMessage, VideoSendMessage

line_bot_api = LineBotApi('TUMeTx6e89YskIYfgtXw7azK/Qp7ghZ7zpG1ftadTfho9Ell85cnos4YHE/j2VYpkW8EcCtoo9Mo85iWp60zeaDWUqXFGulF/MHWb23P92wkQf0IZ3PZY/sz3rCxT/q3JSL1Ia6jcJxgW00XR08uNAdB04t89/1O/w1cDnyilFU=')
# your linebot message API - Channel secret
handler = WebhookHandler('2ab32fa9ab3cf313231d5348e012933f')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

baseurl = 'https://4270-1-164-235-82.ngrok.io/static/'  #靜態檔案網址

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '@傳送聲音':
        try:
            message = AudioSendMessage(
                original_content_url=baseurl + 'mario.m4a',  #聲音檔置於static資料夾
                duration=20000  #聲音長度20秒
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    elif mtext == '@傳送影片':
        try:
            message = VideoSendMessage(
                original_content_url=baseurl + 'robot.mp4',  #影片檔置於static資料夾
                preview_image_url=baseurl + 'robot.jpg'
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)
