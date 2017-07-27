from typing import Iterator


def f(x):
    result = 0
    for i in x:
        result += i
    return result

a = f([1, 2, 3])
b = f({1, 2, 3})
c = f({1: "string", 2: "string2"})


class A:
    def __iter__(self) -> Iterator[int]:
        """ignore body"""
        pass

ca = f(A())


def g(x):
    return len(x)

d = g([1, 2])
e = g("string")


class B:
    def __len__(self):
        pass

cb = g(B())

# a := int
# b := int
# c := int
# d := int
# f := Callable[[Iterable[int]], int]
# g := Callable[[Sized], int]
# ca := int
# cb := int
