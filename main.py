#kalo fork atau clone credit gua jangan diganti yah tod 
#Credit for Mini Music (@triplenineee)

import asyncio
from pytgcalls import idle
from config import call_py
from zhumusic.quote import arq


async def main():
    await call_py.start()
    print(
        """
    ------------------
   | Userbot Started! POWERED BY @triplenineee |
    ------------------
"""
    )
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
