import asyncio
from aioworker import Worker
from dam import App, Topic

loop = asyncio.get_event_loop()


async def hello_world(stream):
    async for value in stream:
        print(value.value)

topics = [
    Topic("test-topic-worker", hello_world),
]

streamapp = App(topics=topics, broker="kafka:0.0.0.0:29092")

Worker(tasks=[streamapp]).run()
