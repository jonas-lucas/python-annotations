"""About annotations using Union Types."""
from typing import Union

# var: str | int | float = 10
var: Union[str, int, float] = 10

def func(user_input: str | int | float) -> None:
    """Sample of function."""
    print(user_input)

func('text')
func(10)
func(10.5)
