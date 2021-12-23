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
import os

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
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id # 發訊者ID

    if msg!='開始': #re.match('[^開始]',message):
        line_bot_api.push_message(uid, TextSendMessage('アニ君無法回應該訊息QwQ \n\n輸入《時間》找尋每日番劇！ \n輸入《今日》探索今日番劇！ \n輸入《類別》查找各類番劇！ \n輸入《#動畫名》查詢動畫資訊！ \n輸入《我的追番》查看收藏番劇！'))
    else:
        message = person_menu()
        line_bot_api.push_message(uid, message)

        
def person_menu():
    flex_message = FlexSendMessage(
        alt_text = "person menu",
        contentS = {
            "type":"bubble",
            # "hero":{
            #     "type":"image",
            #     "url":"",
            #     "size""size": "full",
            #     "aspectRatio": "5:2",
            #     "aspectMode": "cover"
            # },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "人",
                    "weight": "bold",
                    "size": "xl",
                    "align": "center"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "A",
                            "text": "AA小朋友"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "B",
                            "text": "BB小朋友"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "C",
                            "text": "CC小朋友"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "D",
                            "text": "DD小朋友"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "E",
                            "text": "EE小朋友"
                            },
                            "height": "sm",
                            "style": "link"
                        }
                        ],
                        "paddingAll": "none"
                    }
                    ],
                    "paddingAll": "xs"
                }
                ],
                "paddingAll": "md"
            }
        }
    )
    return flex_message



#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)