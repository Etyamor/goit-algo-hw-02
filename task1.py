import queue
import random
import time

request_queue = queue.Queue()


def generate_request(request_id):
    request = {
        'id': request_id,
        'description': f"Заявка #{request_id}",
        'status': 'Нова'
    }
    request_queue.put(request)
    print(f"Згенеровано: {request}")


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        request['status'] = 'Обробляється'
        print(f"Обробка: {request}")
        time.sleep(random.uniform(0.5, 2))
        request['status'] = 'Завершено'
        print(f"Заявка завершена: {request}")
    else:
        print("Черга порожня, немає заявок для обробки.")


def main():
    request_id = 1

    for _ in range(random.randint(4, 6)):
        generate_request(request_id)
        request_id += 1

    try:
        while True:
            generate_request(request_id)
            request_id += 1
            process_request()
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nПрограма зупинена.")


if __name__ == "__main__":
    main()
