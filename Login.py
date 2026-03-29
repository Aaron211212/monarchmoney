import asyncio
from monarchmoney import MonarchMoney

async def main():
    mm = MonarchMoney()
    await mm.interactive_login()  # prompts email, password, MFA
    mm.save_session()
    print("Your token:", mm.token)

asyncio.run(main())