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
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
 
                if event.message.text == "哈囉":
 
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='Menu',
                                text='請選擇地區',
                                actions=[
                                    PostbackTemplateAction(
                                        label='台北市',
                                        text='台北市',
                                        data='A&台北市'
                                    ),
                                    PostbackTemplateAction(
                                        label='台中市',
                                        text='台中市',
                                        data='A&台中市'
                                    ),
                                    PostbackTemplateAction(
                                        label='高雄市',
                                        text='高雄市',
                                        data='A&高雄市'
                                    )
                                ]
                            )
                        )
                    )
            elif isinstance(event, PostbackEvent):  # 如果有回傳值事件
 
                if event.postback.data[0:1] == "A":  # 如果回傳值為「選擇地區」
 
                    area = event.postback.data[2:]  # 透過切割字串取得地區文字
 
                    line_bot_api.reply_message(   # 回復「選擇美食類別」按鈕樣板訊息
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='Menu',
                                text='請選擇美食類別',
                                actions=[
                                    PostbackTemplateAction(  # 將第一步驟選擇的地區，包含在第二步驟的資料中
                                        label='火鍋',
                                        text='火鍋',
                                        data='B&' + area + '&火鍋'
                                    ),
                                    PostbackTemplateAction(
                                        label='早午餐',
                                        text='早午餐',
                                        data='B&' + area + '&早午餐'
                                    ),
                                    PostbackTemplateAction(
                                        label='約會餐廳',
                                        text='約會餐廳',
                                        data='B&' + area + '&約會餐廳'
                                    )
                                ]
                            )
                        )
                    )
 
                elif event.postback.data[0:1] == "B":  # 如果回傳值為「選擇美食類別」
 
                    result = event.postback.data[2:].split('&')  # 回傳值的字串切割
 
                    food = IFoodie(
                        result[0],  # 地區
                        result[1]  # 美食類別
                    )
 
                    line_bot_api.reply_message(  # 回復訊息文字
                        event.reply_token,
                        # 爬取該地區正在營業，且符合所選擇的美食類別的前五大最高人氣餐廳
                        TextSendMessage(text=food.scrape())
                    )
 
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
        
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)