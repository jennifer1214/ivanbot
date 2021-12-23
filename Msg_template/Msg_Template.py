from linebot.models import *

# 星期選單
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
                    "text": "番劇時間",
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
                            "label": "週一",
                            "text": "星期一番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週二",
                            "text": "星期二番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週三",
                            "text": "星期三番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        }
                        ],
                        "paddingAll": "none"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週四",
                            "text": "星期四番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週五",
                            "text": "星期五番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週六",
                            "text": "星期六番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週日",
                            "text": "星期日番劇查詢"
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
