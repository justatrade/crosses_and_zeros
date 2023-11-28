class Move:
    def __init__(self, field_size: int, first: str, second: str) -> None:
        self.queue = []
        self.sign = {first: 'X', second: '0'}
        for i in range(field_size**2):
            if i % 2 == 0:
                self.queue.append(first)
            else:
                self.queue.append(second)
        self.queue = self.queue[::-1]

    def next_move(self) -> str:
        return self.queue[-1]

    def move_done(self) -> None:
        self.queue.pop()