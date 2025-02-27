Design your implementation of the circular double-ended queue (deque).

Implement the Queue class:

- Queue(size) Initializes the deque with a maximum size of "size".
- bool append_right() Adds an item at the tail of Deque. Returns true if the operation is successful, or false otherwise.
- bool append_left() Adds an item at the head of Deque. Returns true if the operation is successful, or false otherwise.
- bool delete_right() Deletes an item from the tail of Deque. Returns true if the operation is successful, or false otherwise.
- bool delete_left() Deletes an item from the head of Deque. Returns true if the operation is successful, or false otherwise.
- int get_right() Returns the tail item from the Deque. Returns -1 if the deque is empty.
- int get_left() Returns the head item from Deque. Returns -1 if the deque is empty.
- bool is_empty() Returns true if the deque is empty, or false otherwise.
- bool is_full() Returns true if the deque is full, or false otherwise.


```python
from typing import Any


class Queue:
    def __init__(self, size: int) -> None:
        ...
    
    def append_right(self) -> bool: # o(1)
        ...
    
    def append_left(self) -> bool: # o(1)
        ...
    
    def delete_right(self) -> bool: # o(1)
        ...

    def delete_left(self) -> bool: # o(1)
        ...

    def get_right(self) -> int: # o(1)
        ...
    
    def get_left(self) -> int: # o(1)
        ...

    def is_empty(self) -> bool: # o(1)
        ...

    def is_full(self) -> bool: # o(1)
        ...
```