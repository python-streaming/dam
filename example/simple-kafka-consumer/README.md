# Simple kafka consumer example

1. Run docker compose

```bash
docker-compose up
```

2. Install requirmeents

```bash
pip install -r requirements.txt
```

3. Run the code from the root folder of dam

```bash
python example/simple-kafka-consumer.py
```

4. Send events

Open a producer console

```bash
docker-compose exec kafka kafka-console-producer --broker-list kafka:9092 --topic test-topic-worker
```
