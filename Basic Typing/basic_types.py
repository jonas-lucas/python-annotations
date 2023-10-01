"""About annotations of Baisc Types."""
text: str = 'hello'
number: int = 10
percent: float = 0.50
connected: bool = False

# def format_input(user_input): # Without Annotation
#     """Sample of funtion."""
#     print(user_input.capitalize())
#
# help(format_input)
#
# Help on function format_input in module __main__:
#
# format_input(user_input)
#

def format_input(user_input: str) -> None:
    """Sample of funtion."""
    print(user_input.capitalize())

help(format_input)
# Help on function format_input in module __main__:
#
# format_input(user_input: str) -> None
#
