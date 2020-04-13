# pync
A simple implementation of netcat in Python.

Great for doing capture the flag on Windows, netcat implementation on python only available on Kali (`pwn`), so I had to make a way around with socket
programming with `socket` in Python.


```
import pync

conn = pync.Pync()
print(conn.receive())
conn.send("answer")
```

#### Available implementation:

- `Pync.receive()`

Receives data. You can define how many bytes to receive on each `receive()` Returns a string.

- `Pync.send(data)`

Sends data. Returns nothing. Needs `data` string message to send.

#### WIP implementation:

- `Pync.receive_all()`

Receive until the end of connection. Somehow it's still buggy.

- `Pync.receive_until(keyword)`

Receive from beginning until the specified `keyword`. Hadn't tested it.

- `Pync.receive_from(keyword)`

Receive from specified `keyword` come up until the end. Hadn't tested it.

- `Pync.sendall(data)`

Same as `Pync.send(data)` but using `sendall()` instead of `send`.

Cheers.
