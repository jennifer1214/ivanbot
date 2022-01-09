#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

line_bot_api.push_message('Ufa79e88066b7a65bae8d131a1f1f9a0c', TextSendMessage(text='請點選下方選單或輸入：開始'))

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
        alt_text='請點餐',
        template=ButtonsTemplate(
            thumbnail_image_url='https://github.com/jennifer1214/ivanbot/blob/main/%E9%BB%9E%E9%A4%90.png?raw=true',
            title='這是你期待已久的一天，校內除了各式各樣的小攤位還不同社團精心策劃的表演',
            text='今天就是一年一度的校慶園遊會。趁著班上攤位的空擋想出去逛逛，這時你會找？',
            actions=[
                PostbackAction(
                    label='A.鄰座的禁慾高冷系同學',
                    display_text='你選擇了鄰座的禁慾高冷系同學',
                    data='1a'
                ),
                PostbackAction(
                    label='B.班上的陽光開朗型同學',
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
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你拉著鄰座的同學一起衝出了教室，走到樓梯口後，你會？',
                text='你選擇了鄰座的禁慾高冷系同學：',
                actions=[
                    PostbackAction(
                            label='A.先去逛攤位',
                            display_text='當然先去逛攤位～',
                            data='1a-2a'
                            ),
                    PostbackAction(
                            label='B.先去看社團展演',
                            display_text='當然先去看社團展演～',
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
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你拉著陽光同學一起衝出了教室，走到樓梯口後，你會？',
                text='你選擇了班上的陽光開朗型同學',
                actions=[
                    PostbackAction(
                            label='A.去大操場逛逛',
                            display_text='操場逛逛～',
                            data='1b-2a'
                            ),
                    PostbackAction(
                            label='B.去逛班級攤位',
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
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='就在這時你們走到大操場，突然有一個足球飛過來，這時你會？',
                text='你選擇了去大操場逛逛，一路上陽光同學都跟你有說有笑',
                actions=[
                    PostbackAction(
                            label='A.抱頭蹲下',
                            display_text='抱頭蹲下～',
                            data='1b-2a-3a'
                            ),
                    PostbackAction(
                            label='B.帥氣得踢回去',
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
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='陽光同學帥氣的把球踢回去，因拒絕不了場上同學的比賽邀約，當結束時休息時間也結束了',
                text='遊戲失敗，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='是',
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
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='陽光同學被你這一球驚艷到，問你要不要一起比一場，這時你會？',
                text='你選擇了帥氣得踢回去',
                actions=[
                    PostbackAction(
                            label='A.先去買吃的',
                            display_text='改天再比吧先去買吃的',
                            data='1b-2a-3b-4a'
                            ),
                    PostbackAction(
                            label='B.比一場',
                            display_text='好呀，來比一場',
                            data='1b-2a-3b-4b'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2a-3b-4a':  
        Carousel_template = TemplateSendMessage(
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='被你這麼一說，陽光同學也覺得有些餓了，這時你會去買？',
                text='你選擇了去買吃的',
                actions=[
                    PostbackAction(
                            label='A.串燒！',
                            display_text='串燒！',
                            data='1b-2a-3b-4a-5a'
                            ),
                    PostbackAction(
                            label='B.辣炒年糕',
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
        alt_text='餐點已抵達，請給5星好評',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='串燒邊走邊吃很方便，你買了一些在回教室的路上和陽光同學一起享用。',
                text='之後你們也時常一起聊天，關係變得更好了。恭喜攻略成功，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='是',
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
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你買了一碗和陽光同學分著吃，之後就回教室值班。',
                text='隔天校方公佈賣辣炒年糕的班級有人是新冠肺炎無症狀確診者，很不幸的你們兩個吃完後都中標了。遊戲失敗，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='是',
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
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你們開開心心的比完了一場後休息時間也差不多結束了，你們匆匆忙忙地回教室。',
                text='之後陽光同學似乎因為你球踢得好，一直把你當兄弟TAT。恭喜達成『我們是好兄弟』成就，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2b':  
        Carousel_template = TemplateSendMessage(
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你拉著陽光同學一起衝出了教室，走到樓梯口後，你會？',
                text='你選擇了去大操場逛逛，一路上陽光同學都跟你有說有笑',
                actions=[
                    PostbackAction(
                            label='A.一班的女僕咖啡',
                            display_text='女僕咖啡',
                            data='1b-2b-3a'
                            ),
                    PostbackAction(
                            label='B.三班的二手市集',
                            display_text='二手市集',
                            data='1b-2b-3b'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2b-3a':  
        Carousel_template = TemplateSendMessage(
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你和陽光同學一同入座後，你會點？',
                text='你選擇了去女僕咖啡',
                actions=[
                    PostbackAction(
                            label='A.草莓聖代',
                            display_text='草莓聖代，兩人分著吃感情更升溫',
                            data='1b-2b-3a-4a'
                            ),
                    PostbackAction(
                            label='B.原味鬆餅',
                            display_text='原味鬆餅，兩人分著吃感情更升溫',
                            data='1b-2b-3a-4b'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2b-3a-4a':  #路線13 END
        Carousel_template = TemplateSendMessage(
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='陽光同學看似大大咧咧，但其實重度潔癖。聖代雖然浪漫，但融化的太快到後面看起來噁心',
                text='陽光同學接受不了，好感度歸零。遊戲失敗，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2b-3a-4b':  
        Carousel_template = TemplateSendMessage(
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你們兩個人有說有笑的吃著鬆餅討論著等一下一要去逛哪裡，這時你會？',
                text='你選擇了原味鬆餅',
                actions=[
                    PostbackAction(
                            label='A.看陽光同學想逛哪裡',
                            display_text='陽光同學想逛哪裡',
                            data='1b-2b-3a-4b-5a'
                            ),
                    PostbackAction(
                            label='B.去逛三班的二手市集',
                            display_text='二手市集',
                            data='1b-2b-3a-4b-5b'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2b-3a-4b-5a':  #路線14 END
        Carousel_template = TemplateSendMessage(
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='陽光同學選擇了去大操場跟朋友們踢足球，你默默的在旁邊看著，就這樣休息時間結束',
                text='最後沒有跟陽光同學增近到感情。遊戲失敗，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2b-3a-4b-5b':  #路線15 END
        Carousel_template = TemplateSendMessage(
        alt_text='餐點已抵達，請給5星好評',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='陽光同學早就聽說二手市集很有趣於是便一起去逛了二手市集，你們度過了愉快的時光',
                text='之後陽光同學也會時不時的約你出去。恭喜遊戲成功!是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1b-2b-3b':  #路線16 END
        Carousel_template = TemplateSendMessage(
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='陽光同學表示想吃東西，導致意見分歧。最後他不情願的先陪妳去了二手市集',
                text='好感度直接歸零。遊戲失敗，是否要重新開始遊戲？',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1a-2a':  
        Carousel_template = TemplateSendMessage(
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='眼前是各個班級擺放的攤位，有吃得有玩的。忙了一個早上，你會先？',
                text='你選擇了先去逛攤位',
                actions=[
                    PostbackAction(
                            label='A.去買吃的。',
                            display_text='去買吃的。',
                            data='1a-2a-3a'
                            ),
                    PostbackAction(
                            label='B.去玩遊戲。',
                            display_text='去玩遊戲。',
                            data='1a-2a-3b'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1a-2b':  
        Carousel_template = TemplateSendMessage(
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你們走到了學校的大禮堂，發現眼前有許多不同的社團，這時你會?',
                text='你選擇了先去看社團展演',
                actions=[
                    PostbackAction(
                            label='A.去話劇社的鬼屋',
                            display_text='去話劇社的鬼屋',
                            data='1a-2b-3a'
                            ),
                    PostbackAction(
                            label='B.去占卜社的塔羅牌攤位',
                            display_text='去占卜社的塔羅牌攤位',
                            data='1a-2b-3b'
                            )
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template) 
    #路線五結尾
    elif event.postback.data == '1a-2b-3a':  
        Carousel_template = TemplateSendMessage(
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='鄰座的同學雖然是個高冷系，但其實怕黑怕鬼。被你拉去鬼屋後，他就不怎麼理你了',
                text='失敗，是否要重新開始',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1a-2b-3b':  
        Carousel_template = TemplateSendMessage(
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你來到了塔羅牌攤位，拉著同學一起坐了下來，這時你會想算?',
                text='你選擇了去占卜社的塔羅牌攤位',
                actions=[
                    PostbackAction(
                            label='A.當然是算愛情 ',
                            display_text='當然是算愛情',
                            data='1a-2b-3b-4a'
                            ),
                    PostbackAction(
                            label='B.當然是算學業 ',
                            display_text='當然是算學業 ',
                            data='1a-2b-3b-4b'
                            )
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template) 
    #路線六結尾
    elif event.postback.data == '1a-2b-3b-4a':  
        Carousel_template = TemplateSendMessage(
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='同學就一個鋼鐵直男，此時此刻內心OS大概是：怎麼不算算學業？數學作業都抄我的呢',
                text='失敗，是否要重新開始',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1a-2b-3b-4b':  
        Carousel_template = TemplateSendMessage(
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='算出結果似乎是缺乏動力和耐心，這時你會?',
                text='你選擇了當然是算學業',
                actions=[
                    PostbackAction(
                            label='A.占卜不可太迷性',
                            display_text='占卜不可太迷性，參考就好',
                            data='1a-2b-3b-4b-5a'
                            ),
                    PostbackAction(
                            label='B.請鄰座的同學教你課業 ',
                            display_text='請鄰座的同學教你課業 ',
                            data='1a-2b-3b-4b-5b'
                            )
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)    
    #路線七結尾
    elif event.postback.data == '1a-2b-3b-4b-5a':  
        Carousel_template = TemplateSendMessage(
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='鄰座的同學表示：你平常都在抄我的作業了，不該好好努力一下嗎？',
                text='失敗，是否要重新開始',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
        
    #路線八結尾
    elif event.postback.data == '1a-2b-3b-4b-5b':  
        Carousel_template = TemplateSendMessage(
        alt_text='餐點已抵達，請給5星好評',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='每天下課你都會跟鄰座的同學去圖書館讀書，好感度刷刷的往上加～',
                text='成功，恭喜攻略對象!是否要重新開始?',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template) 
    elif event.postback.data == '1a-2a-3a':  
        Carousel_template = TemplateSendMessage(
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='你在猶豫要吃辣吵年糕還是臭豆腐，這時你會？',
                text='你選擇了去買吃的',
                actions=[
                    PostbackAction(
                            label='A.問鄰座同學該吃哪一個',
                            display_text='問鄰座同學該吃哪一個',
                            data='1a-2a-3a-4a'
                            ),
                    PostbackAction(
                            label='B.兩個都買反正我很餓',
                            display_text='兩個都買反正我很餓',
                            data='1a-2a-3a-4b'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    
    #路線四結尾
    elif event.postback.data == '1a-2a-3b':  
        Carousel_template = TemplateSendMessage(
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='鄰座的同學其實很餓，只想去買點吃的才跟你出來。沒想會被你拉去玩遊戲',
                text='你似乎被討厭了。失敗，是否要重新開始',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.postback.data == '1a-2a-3a-4a':  
        Carousel_template = TemplateSendMessage(
        alt_text='送餐中．．．',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='鄰座同學提議兩個都買，你們可以各一人一半。這時你會？',
                text='你選擇了問問鄰座同學該吃哪一個',
                actions=[
                    PostbackAction(
                            label='A.接受提案',
                            display_text='接受提案拉近兩人的距離。',
                            data='1a-2a-3a-4a-5a'
                            ),
                    PostbackAction(
                            label='B.感覺不太好最後都沒買',
                            display_text='感覺不太好最後都沒買 。',
                            data='1a-2a-3a-4a-5b'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)

    #路線三結尾
    elif event.postback.data == '1a-2a-3a-4b':  
        Carousel_template = TemplateSendMessage(
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='鄰座的同學覺得很無聊，完全被當空氣。你的好感度被降為負分。',
                text='失敗，是否要重新開始',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    #路線一結尾
    elif event.postback.data == '1a-2a-3a-4a-5a':  
        Carousel_template = TemplateSendMessage(
        alt_text='運送過程發生錯誤，請重新點餐',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='賣辣炒年糕的班級有人是新冠肺炎無症狀確診者，很不幸的你們兩個吃完後都中標',
                text='失敗，是否要重新開始',
                actions=[
                    PostbackAction(
                            label='是',
                            text='重新開始',
                            data='開始'
                            )
                ]
            )
        ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)

#路線二結尾
    elif event.postback.data == '1a-2a-3a-4a-5b':  
        Carousel_template = TemplateSendMessage(
        alt_text='餐點已抵達，請給5星好評',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='園遊會後學校緊急公佈賣辣炒年糕的班級有肺炎確診者，直接停課大清消。',
                text='鄰座的同學表示感謝你當初的明智之舉，之後你們反而變得更親密～成功，恭喜攻略對象！是否要重新開始?',
                actions=[
                    PostbackAction(
                            label='是',
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

