import asyncio
from typing import List, Optional


class App:
    def __init__(
        self,
        broker: str,
        topics: Optional[List] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ):
        if loop is None:
            loop = asyncio.get_event_loop()
        self.loop = loop
        self.topics = topics
        self.broker, self.hostname = broker.split(":", 1)

    async def run(self):
        for topic in self.topics:
            topic._configure({
                "bootstrap_servers": self.hostname
            })
            await topic.run()

    async def __call__(self, loop):
        if loop is not None:
            self.loop = loop
        await self.run()
