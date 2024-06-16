import threading
import time

import rabbitmq.consumer
import rabbitmq.processor
from utils.container_checker import check_containers_state


def main():
    time.sleep(30)

    status_thread = threading.Thread(target=check_containers_state)
    status_thread.daemon = True
    status_thread.start()

    # Number of consumer threads
    num_threads = 2

    # Create a pool of threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(
            target=rabbitmq.consumer.consume_messages,
            args=(rabbitmq.processor.process_message,),
        )
        thread.daemon = True
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
