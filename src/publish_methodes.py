from google.cloud import pubsub_v1
from concurrent import futures


def publish_messages_with_batch_settings(
    topic_path: str, num_of_messages: int, batch_settings, data
) -> int:
    """Publishes multiple messages to a Pub/Sub topic with batch settings."""
    batch_settings = pubsub_v1.types.BatchSettings(
        max_messages=batch_settings["maxMessages"],
        max_bytes=batch_settings["maxBytes"],
        max_latency=batch_settings["maxLatency"],
    )
    publisher = pubsub_v1.PublisherClient(batch_settings)
    publish_futures = []

    def callback(future: pubsub_v1.publisher.futures.Future) -> None:
        message_id = future.result()
        print(message_id)

    for n in range(1, num_of_messages):

        publish_future = publisher.publish(
            topic_path, data, origin="python", username="batch"
        )
        publish_future.add_done_callback(callback)
        publish_futures.append(publish_future)

    futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)
    print(f"Published messages with batch settings to {topic_path}.")
    return len(publish_futures)


def publish_messages(topic_path, num_of_messages: int, data, *args) -> int:
    """Publishes multiple messages to a Pub/Sub topic."""

    publisher = pubsub_v1.PublisherClient()

    for n in range(1, num_of_messages):
        future = publisher.publish(topic_path, data, origin="python", username="stream")
        print(future.result())

    print(f"Published messages to {topic_path}.")
    return len(future.result())
