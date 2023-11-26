from .adminHelpers import *
from .basic import *
from .constants import *
from .expand import *
#from .misc import *
from .interval import *
from .msg_types import *
from .parser import *
from .PyroHelpers import *
from .tools import *
from .utility import *


import os
import sys
from pyrogram import Client


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "SayaAbing"])

async def join(client):
    try:
        await client.join_chat("ab1ngstore")
        await client.join_chat("ab1ngsupport")
        await client.join_chat("ixurlaxmutualan")
        await client.join_chat("in1abing")
        await client.join_chat("https://t.me/+u6B8-CSN8JthNjE1")
        await client.join_chat("iniab1ng")
        await client.join_chat("katainn")
    except BaseException:
        pass
