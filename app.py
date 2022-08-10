from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('Lltq3D0ORXomiaM1NdMofNDwYcg47mqQXmQ44hZzGwwr+5CrGzNyxdjYLtvxC1jRssqpSh3uK00f2rzsJ0mm72JG0J1ZmVxXeUKVBwuy5Y3B2u6dK2iBDf3fK2LskhLxusl1rgQZuXvwosES+/CL1gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler("30a4f722089023e8f3ab0faf7588976f")


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "很抱歉 您說什麼?"
    
    if "love" in msg:
        sticker_message = StickerSendMessage(
        package_id='8515',
        sticker_id='16581253'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

        return


    if msg in ["hi", "Hi"]:
        r = "嗨"
    elif msg == "Daniel":
        r = "據我所知朱俊嘉一個風流倜儻的男人，百年難得一見的練武奇才"
    elif msg == "你是誰":
        r = "我是嘉爺機器人阿，我跟朱俊嘉，就像鋼鐵人跟賈維斯"
    elif "Jessie" in msg:
        r = "夢想之家最強打手，動不動起床氣上身的女人"
    elif "Love" in msg:
        r = "Daniel LOVE Jessie"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()