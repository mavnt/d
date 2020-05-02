# d

Shorthand property names (ES2015) for Python dictionaries.

## Example

```python
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
```

```
{
    "another_value": 1,
    "user1": {
        "name": "John",
        "surname": "Smith",
        "age": 99,
        "data": [
            1,
            2,
            3,
            5
        ]
    },
    "time_": 1588446844.5190823
}
```

## Note

This works best with **mutable objects**. See following examples.

```python
import json

from d import d


def main():
    a = 0
    b = 0
    print(json.dumps(d(a=0), indent=4,))

    # ValueError: duplicate key for 0
    # otherwise b: 0 would have been included in the dictionary
    # since a is b => True
    print(json.dumps(d(a), indent=4,))


if __name__ == "__main__":
    main()
```
