import azure
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
    MessageEvent, TextMessage, TextSendMessage,
)
# create flask server
app = Flask(__name__)
# your linebot message API - Channel access token (from LINE Developer)
line_bot_api = LineBotApi('IPlA3rOBc1lT+ubgYl/zyRmA3lFdSZKLJWLSZya6hBy4qFPtqMV6k+bWbZxv9LfakW8EcCtoo9Mo85iWp60zeaDWUqXFGulF/MHWb23P92yAI2WZbKUCnibssNMznxhK/IaoSYG0rrxLzZp6yIMu6AdB04t89/1O/w1cDnyilFU=')
# your linebot message API - Channel secret
handler = WebhookHandler('cc218d13a298f6a8fde93c2ecda97203')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        print('receive msg')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# handle msg
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user info & message
    user_id = event.source.user_id
    msg = event.message.text
    re = azure.az(msg)
    # get msg details
    # push text_msg
    line_bot_api.reply_message(TextSendMessage(text = re))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345,debug=True)