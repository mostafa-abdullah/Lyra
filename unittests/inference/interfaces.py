def f(x):
    result = 0
    for i in x:
        result += i
    return result

a = f([1, 2, 3])
b = f({1, 2, 3})
c = f({1: "string", 2: "string2"})


def g(x):
    return len(x)

d = g([1, 2])
e = g("string")

# a := int
# b := int
# c := int
# d := int
# f := Callable[[Iterable[int]], int]
# g := Callable[[Sized], int]

