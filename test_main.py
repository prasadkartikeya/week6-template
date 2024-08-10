def test_counter():
    from main import counter

    counter1 = counter()
    counter2 = counter()

    for i in range(1, 5):
        assert counter1() == i

    for i in range(1, 10):
        assert counter2() == i

    assert counter1() == 5
    assert counter()() == 1


def test_multiplier():
    from main import multiplier
    from random import randint

    for i in range(10):
        n = randint(1, 100)
        assert multiplier(i)(n) == i * n
