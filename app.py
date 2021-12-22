# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
選擇按鈕ConfirmTemplate
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('2bA2+2BpXpPhMxU5Mn6MJNanrwhM75WyW/bFDHUjbYIrdB8cufjwH2MocJllX7W/0wnv55EIZtJUVCn5M2/kG8N4tqPx2coDmGFfFdBZPJp64AfGRrkFpn3T5Bs9C06KlgwPTZrRFHAzdG3Xz90ReQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('7ab781240bed864ae1ae0e554acf3475')

line_bot_api.push_message('Ufa79e88066b7a65bae8d131a1f1f9a0c', TextSendMessage(text='開始你的表演，請輸入：開始'))

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('[^開始]',message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
    else:
        confirm_template_message = TemplateSendMessage(
            alt_text='問問題',
            template=ConfirmTemplate(
                text='你喜歡的是？',
                actions=[
                    PostbackAction(
                        label='男生',
                        display_text='我選擇男生',
                        data='action=男生'
                    ),
                    PostbackAction(
                        label='女生',
                        display_text='我選擇女生',
                        data='action=女生'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
        if re.match('[我選擇男生]',confirm_template_message):
            line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
        else:
            confirm_template_message = TemplateSendMessage(
                alt_text='問問題',
                template=ConfirmTemplate(
                    text='你選擇男生，那喜歡的是？',
                    actions=[
                        PostbackAction(
                            label='男生',
                            display_text='我選擇男生',
                            data='action=男生'
                        ),
                        PostbackAction(
                            label='女生',
                            display_text='我選擇女生',
                            data='action=女生'
                        )
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
        
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)