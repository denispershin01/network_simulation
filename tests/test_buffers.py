from network_protocols.logic.buffers import Message, Queue


def test_buffer_length() -> None:
    queue = Queue()

    queue.put(Message("1"))
    queue.put(Message("2"))
    queue.put(Message("3"))

    assert queue.length == 3


def test_buffer_pop() -> None:
    queue = Queue()
    message_count = 5
    messages = [Message(str(i)) for i in range(message_count)]

    for message in messages:
        queue.put(message)

    for i in range(message_count):
        assert queue.pop() == messages[i]


def test_buffer_put() -> None:
    queue = Queue()
    message_count = 5
    messages = [Message(str(i)) for i in range(message_count)]

    for message in messages:
        queue.put(message)

    assert queue.length == message_count


def test_buffer_pop_empty() -> None:
    queue = Queue()

    assert queue.pop() is None


def test__empty_buffer_length() -> None:
    queue = Queue()

    assert queue.length == 0
