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

line_bot_api.push_message('Ufa79e88066b7a65bae8d131a1f1f9a0c', TextSendMessage(text='心頭的硃砂痣，床前的白月光。都是愛而不得的初戀一個個寂寞的夜，一杯杯傷情的酒。都是用來告別那些痛而不忘，恨而不舍的單戀，請輸入：開始'))

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
    if re.match('開始',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='這個看不到',
        template=ButtonsTemplate(
            thumbnail_image_url='https://raw.githubusercontent.com/jennifer1214/ivanbot/main/%E6%9C%AA%E5%91%BD%E5%90%8D.png',
            title='還是單身狗？不用擔心，歡迎公測這款全新戀愛養成遊戲即刻下載就送十連，再送大禮包',
            text='Q. 請選擇你的攻略對象。',
            actions=[
                PostbackAction(
                    label='A. 禁慾高冷係',
                    display_text='你選擇了禁慾高冷係',
                    data='1-a'
                ),
                PostbackAction(
                    label='B. 黏人小奶狗',
                    display_text='你選擇了黏人小奶狗',
                    data='1-b'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('bye'))


@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == '1-a':  
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你選擇了禁慾高冷係：',
                text='Q. 今天第一天約會，要穿什麼勒？',
                actions=[
                    PostbackAction(
                            label='A. 日系甜美風。',
                            text='這麼高冷，當然要用我可愛的外表溫暖你的心～',
                            data='A-2-a'
                            ),
                    PostbackAction(
                            label='B. 高冷御姐風。',
                            text='約會當然要配合我家歐爸，站在一起才是神仙眷侶～',
                            data='A-2-b'
                            ),
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1-b':  
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你選擇了黏人小奶狗：',
                text='Q. 今天第一天約會，要穿什麼勒？',
                actions=[
                    PostbackAction(
                            label='A. 慵懶運動風。',
                            text='我不管穿什麼都是女神，慵懶係不在話下～',
                            data='B-2-a'
                            ),
                    PostbackAction(
                            label='B. 英倫學院風。',
                            text='可鹽可甜，不怕踩雷，第一次約會妥妥過啦～',
                            data='B-2-b'
                            ),
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)    

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)