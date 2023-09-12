import asyncio
import httpx
from time import sleep
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 7):
        await asyncio.sleep(1)
        print(num - 1)
    async with httpx.AsyncClient() as client:
        r = await client.get('https://httpbin.org')
        print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('----This is an async view it`s working!----')