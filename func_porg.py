from  typing import TypeVar, Callable, Sequence, Iterator

T = TypeVar("T")
U = TypeVar("U")


class Seq:
    def __init__(self, sequence: (Sequence[T] | Iterator[T])):
        self.gen = iter(sequence)

    def map(self, func: Callable[[T], U]):
        def gen():
            for x in self.gen:
                yield func(x)
        return Seq(gen())

    def filter(self, filter: Callable[[T], bool]):
        def gen():
            for x in self.gen:
                if filter(x):
                    yield x
        return Seq(gen())

    def take(self, n: int):
        res = []
        for i in range(n):
            try:
                res.append(next(self.gen))
            except StopIteration:
                break
        return res


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    seq = Seq(numbers)
    res = seq.filter(lambda n: n % 2 == 0).map(lambda n: n + 10).take(3)
    print(res)
