import json
import time

from d import d


def main():
    time_ = time.time()
    user1 = {
        "name": "John",
        "surname": "Smith",
        "age": 99,
        "data": [1, 2, 3, 5],
    }
    user2 = {
        "name": "John",
        "surname": "Smith",
        "age": 99,
        "data": [1, 2, 3, 5],
    }

    print(json.dumps(d(user1, time_, another_value=1), indent=4))


if __name__ == "__main__":
    main()
