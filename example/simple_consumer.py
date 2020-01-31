import asyncio
from dam import App, Topic

loop = asyncio.get_event_loop()


async def hello_world(stream):
    async for value in stream:
        print(value.value)


async def hello_world2(stream):
    async for value in stream:
        print("other topic", value.value)


topics = [
    Topic("test-topic-worker", hello_world),
    Topic("fifo", hello_world2)
]

streamapp = App(topics=topics)

while True:
    # This should be any other worker
    loop.run_until_complete(streamapp.run())
