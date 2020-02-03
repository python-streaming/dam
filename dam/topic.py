import asyncio
from typing import Callable, Dict

from aiokafka import AIOKafkaConsumer, errors

from dam.stream import Stream


class Topic:
    """Kafka topic"""

    def __init__(self, name: str, func: Callable, **kwargs):
        self.name = name
        self.func = func
        self.consumer_kwargs: Dict = kwargs

    def _configure(self, conf: Dict):
        self.conf = conf

    def create_consumer(
        self, name: str, loop: asyncio.AbstractEventLoop = None
    ) -> AIOKafkaConsumer:
        if loop is None:
            loop = asyncio.get_event_loop()

        return AIOKafkaConsumer(
            name,
            loop=loop,
            auto_offset_reset="earliest",
            **self.conf,
            **self.consumer_kwargs
        )

    async def run(self):
        consumer = self.create_consumer(self.name)

        await consumer.start()

        try:
            # Consume messages
            await self.func(Stream(consumer))
        finally:
            # Will leave consumer group; perform autocommit if enabled.
            await consumer.stop()
