import asyncio
from typing import List, Optional


class App:
    def __init__(
        self,
        topics: Optional[List] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ):
        if loop is None:
            loop = asyncio.get_event_loop()
        self.loop = loop
        self.topics = topics

    async def run(self):
        for topic in self.topics:
            await topic.run()
