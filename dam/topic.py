import asyncio
from typing import Callable

from aiokafka import AIOKafkaConsumer

from dam.stream import Stream


class Topic:
    """Kafka topic"""

    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func

    def create_consumer(
        self, name: str, loop: asyncio.AbstractEventLoop = None
    ) -> AIOKafkaConsumer:
        if loop is None:
            loop = asyncio.get_event_loop()

        return AIOKafkaConsumer(
            name,
            loop=loop,
            bootstrap_servers="0.0.0.0:29092",
            group_id="test-consumer-group",
            auto_offset_reset="earliest",
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


# async def consume_from_kafka(loop):
#     logger.debug("Task Consuming from kafka initiated...")
#     consumer = AIOKafkaConsumer(
#         TOPIC,
#         loop=loop,
#         bootstrap_servers=BOOTSTRAP_SERVERS,
#         group_id=GROUP_ID,
#         auto_offset_reset=AUTO_OFFSET_RESET,
#     )

#     # Get cluster layout and join group `my-group`await consumer.start()
#     await consumer.start()

#     try:
#         # Consume messages
#         async for msg in consumer:
#             print(f"Task Consuming from kafka")
#             print(
#                 f"Topic: {msg.topic}, Partition: {msg.partition}, Offset: {msg.offset},"
#                 f" Key: {msg.key}, Value: {msg.value}, Timestamp: {msg.timestamp}\n"
#             )
#     finally:
#         # Will leave consumer group; perform autocommit if enabled.
#         await consumer.stop()
