class Stream:
    def __init__(self, stream):
        self.stream = stream

    async def __aiter__(self):
        async for item in self.stream:
            yield item

    async def __anext__(self):
        raise StopAsyncIteration
