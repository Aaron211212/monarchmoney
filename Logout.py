import asyncio
from monarchmoney import MonarchMoney

async def main():
    mm = MonarchMoney()
    mm.load_session()
    await mm.logout()  # invalidates the token server-side

asyncio.run(main())