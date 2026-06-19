import asyncio
from connection import check_mongo

async def main():
    result = await check_mongo()
    print(f'Connection: {result}')

asyncio.run(main())
