# -*- coding: utf-8 -*-
import asyncio
import blivedm

TEST_AUTH_CODE = 'CWEPYMW57FNK6'
APP_ID = '1651220148034'
ACCESS_KEY = 'HrKeRsqT1wWQQRzsmz2Jksl8'
ACCESS_KEY_SECRET = 'lGT9mC9KK7AiH1WRoVa0KBWpOHXOQx'

class OpenLiveHandlerInterface:
    """
    开放平台直播消息处理器接口
    """

    async def handle(self, client: blivedm.BLiveClient, command: dict):
        print(f'{command}')

async def main():
    await run_start()

async def run_start():
    client = blivedm.BLiveClient(use_open_live=True, open_live_app_id=APP_ID, open_live_access_key=ACCESS_KEY, open_live_access_secret=ACCESS_KEY_SECRET, open_live_code=TEST_AUTH_CODE, ssl=True)
    handler = OpenLiveHandlerInterface()
    client.add_handler(handler)

    client.start()
    try:
        # 演示20秒后停止
        await asyncio.sleep(60)
        client.stop()

        await client.join()
    finally:
        await client.stop_and_close()

if __name__ == '__main__':
    asyncio.run(main())