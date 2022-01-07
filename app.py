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

line_bot_api.push_message('Ufa79e88066b7a65bae8d131a1f1f9a0c', TextSendMessage(text='請輸入：開始'))

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
    if (message=='開始' or message=='重新開始'):
        buttons_template_message = TemplateSendMessage(
        alt_text='這個看不到',
        template=ButtonsTemplate(
            thumbnail_image_url='https://raw.githubusercontent.com/jennifer1214/ivanbot/main/%E6%9C%AA%E5%91%BD%E5%90%8D.png',
            title='這是你期待已久的一天，校內除了各式各樣的小攤位還不同社團精心策劃的表演',
            text='今天就是一年一度的校慶園遊會。趁著班上攤位的空擋想出去逛逛，這時你會找？',
            actions=[
                PostbackAction(
                    label='A. 鄰座的禁慾高冷系同學',
                    display_text='你選擇了鄰座的禁慾高冷系同學係',
                    data='1a'
                ),
                PostbackAction(
                    label='B. 班上的陽光開朗型同學',
                    display_text='你選擇了班上的陽光開朗型同學',
                    data='1b'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('請點選選項，或輸入："開始" 重新遊戲'))


@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == '1a':  
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你拉著鄰座的同學一起衝出了教室，走到樓梯口後，你會？',
                text='你選擇了鄰座的禁慾高冷系同學：',
                actions=[
                    PostbackAction(
                            label='A. 先去逛攤位',
                            display_text='這麼高冷，當然要先去逛攤位～',
                            data='1a-2a'
                            ),
                    PostbackAction(
                            label='B. 先去看表演',
                            display_text='陽光開朗型，先去看表演～',
                            data='1a-2b'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b':  
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你拉著陽光同學一起衝出了教室，走到樓梯口後，你會？',
                text='你選擇了班上的陽光開朗型同學',
                actions=[
                    PostbackAction(
                            label='A. 去大操場逛逛',
                            display_text='操場逛逛～',
                            data='1b-2a'
                            ),
                    PostbackAction(
                            label='B. 去逛班級攤位',
                            display_text='班級攤位～',
                            data='1b-2b'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2a':  
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='就在這時你們走到大操場，突然有一個足球飛過來，這時你會？',
                text='你選擇了去大操場逛逛，一路上陽光同學都跟你有說有笑',
                actions=[
                    PostbackAction(
                            label='A. 到頭蹲下',
                            display_text='到頭蹲下～',
                            data='1b-2a-3a'
                            ),
                    PostbackAction(
                            label='B. 帥氣得踢回去',
                            display_text='帥氣得踢回去～',
                            data='1b-2a-3b'
                            ),
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2a-3a':  #路線9 END
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='陽光同學帥氣的把球踢回去，因拒絕不了場上同學的比賽邀約，當結束時休息時間也結束了',
                text='遊戲失敗，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='A. 是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2a-3b':  
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='陽光同學被你這一球驚艷到，問你要不要一起比一場，這時你會？',
                text='你選擇了帥氣得踢回去',
                actions=[
                    PostbackAction(
                            label='A. 改天再比吧，先去買吃的',
                            display_text='去買吃的',
                            data='1b-2a-3b-4a'
                            ),
                    PostbackAction(
                            label='B. 好呀，來比一場',
                            display_text='比一場',
                            data='1b-2a-3b-4b'
                            ),
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2a-3b-4a':  
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='被你這麼一說，陽光同學也覺得有些餓了，這時你會去買？',
                text='你選擇了去買吃的',
                actions=[
                    PostbackAction(
                            label='A. 串燒！',
                            display_text='串燒！',
                            data='1b-2a-3b-4a-5a'
                            ),
                    PostbackAction(
                            label='B. 辣炒年糕',
                            display_text='辣炒年糕',
                            data='1b-2a-3b-4a-5b'
                            ),
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2a-3b-4a-5a':  #路線10 END
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='串燒邊走邊吃很方便，你買了一些在回教室的路上和陽光同學一起享用。',
                text='之後你們也時常一起聊天，關係變得更好了。恭喜達成友情路線，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='A. 是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2a-3b-4a-5b':  #路線11 END
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你買了一碗和陽光同學分著吃，之後又回就是值班。',
                text='隔天校方公佈賣辣炒年糕的班級有人是新冠肺炎無症狀確診者，很不信的你們兩個吃完後都中標了。遊戲失敗，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='A. 是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2a-3b-4b':  #路線12 END
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你們開開心心的比完了一場後休息時間也差不多結束了，你們衝衝忙忙地回教室。',
                text='之後陽光同學似乎因為你球踢得好，一直把你當兄弟TAT。恭喜達成『我們是好兄弟』成就，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='A. 是',
                            text='重新開始',
                            data='開始'
                            )
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