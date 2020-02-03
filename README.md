# dam

> Python Stream Processing minimalistic toolkit

:warning: WARNING :warning:

_This repo is highly experimental and it's not recommended for production use._

_The interface may change at any time during initial development._

_Still not published to pypi._

```python
import asyncio
from dam import App, Topic

loop = asyncio.get_event_loop()

async def hello_world(stream):
    async for value in stream:
        print(value.value)


topics = [
    Topic("test-topic-worker", hello_world)
]

streamapp = App(topics=topics, broker="kafka:0.0.0.0:29092")

while True:
    # This should be any other worker
    loop.run_until_complete(streamapp.run())
```

## Example

- [simple-kafka-consumer](example/simple-kafka-consumer)

## Usage

1. Clone repository
2. Run `poetry install`
3. Write apps inside `example` folder (for now)
