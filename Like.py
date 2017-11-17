# -*- coding: utf-8 -*-
import LINETHB
from LINETHB.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob
cl = LINETHB.LINE()
print u"""Login START"""
cl.login(qr=True)
cl.loginResult()
print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')
print u"login成功"
i = 0
c_text = """[тεαм вσт gιяℓs]"""


while True:
    try:
        for posts in cl.activity(1)["result"]["posts"]:
            if posts["postInfo"]["liked"] is False:
                cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
                cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],"αυтσ ℓιкє ву ѕρє¢ιαℓ αиιмє/https://line.me/R/ti/p/%40kyx3655e")
                print u"liked" + str(i)
                i += 1
    except Exception as e:
            print e
