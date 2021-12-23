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
import pandas as pd
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

df = pd.read_csv('Q_and_A.csv') 

# def get_tag_color(tag):
#     if tag == "減分":
#         tag_color = "#ED784A"
#     elif tag == "加分":
#         tag_color = "#FF334B"

#     return tag_color

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('2bA2+2BpXpPhMxU5Mn6MJNanrwhM75WyW/bFDHUjbYIrdB8cufjwH2MocJllX7W/0wnv55EIZtJUVCn5M2/kG8N4tqPx2coDmGFfFdBZPJp64AfGRrkFpn3T5Bs9C06KlgwPTZrRFHAzdG3Xz90ReQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('7ab781240bed864ae1ae0e554acf3475')

line_bot_api.push_message('Ufa79e88066b7a65bae8d131a1f1f9a0c', TextSendMessage(text='歡迎光臨，請輸入：開始'))

with open("control.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("Ufa79e88066b7a65bae8d131a1f1f9a0c", "image/jpeg", f)

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

    if re.match("開始", msg):
        message = week_menu()
        line_bot_api.push_message(uid, message)
    elif re.match(r'AA|BB', msg):
        ani_data = Ani_info.get_category_data(msg)
        message = ani_category(msg, ani_data)
        line_bot_api.push_message(uid, message)
    else:
        line_bot_api.push_message(uid, TextSendMessage('bye'))

def week_menu(): 
    flex_message = FlexSendMessage(
        alt_text = "Time Menu",
        contents = {
            "type": "bubble",
            # "hero": {
            #     "type": "image",
            #     "url": "https://i.imgur.com/1sKXwFc.png",
            #     "size": "full",
            #     "aspectRatio": "5:2",
            #     "aspectMode": "cover"
            # },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "選擇",
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
                            "text": "AA"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "B",
                            "text": "BB"
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


def get_category_data(ani_cate):
    data = df[df[ani_cate] == 1]
    data.reset_index(inplace=True)
    name = list(data.A1.values)
    intro = list(data.A1結果.values)
    # image = list(data.封面.values)
    # tag = list(data.Tag.values)
    # tag_color = [get_tag_color(x) for x in tag]
    return name, intro#, image, tag, tag_color
    


#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)