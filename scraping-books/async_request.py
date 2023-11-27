# 1
# import aiohttp
# import asyncio

# async def fetch_page(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             print(response.status)
#             return response.status

# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch_page('http://google.com'))


import asyncio
import async_timeout
import aiohttp
import time

async def fetch_page(session, url):
    start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return response.status


async def get_multiple_pages(loop, *urls):
    pages = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            pages.append(await fetch_page(session, url))
    return pages


if __name__ == '__main__':

    def main():
        loop = asyncio.get_event_loop()
        urls = [
            'http://google.com',
            'http://example.com',
            'http://tecladocode.com/blog'
        ]
        start = time.time()
        pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
        print(f'Total took {time.time() - start}')
        for page in pages:
            print(page)

    main()