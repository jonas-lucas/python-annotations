"""About annotations of Lists."""
elements: list[int] = [1, 2, 3, 4, 5]

names: list[str] = ['Jonas', 'Lucas']

mixed: list[str | int] = ['a', 1]

nested: list[list[str]] = [['a', 'b'], ['c', 'd']]

uncaught_list: list[int | None | str] = [10, None, 'hello']
