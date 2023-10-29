y_dict: dict[str, int] = {'a': 10, 'b': 20}

def print_it(some_dict: dict[int, str]):
	for value in some_dict.values():
		print(value.title())

example: dict[int, str] = {1: 'jonas', 2: 'lucas'}

print_it(example)

# my_dict2: dict[str, int] = {'a': 10}
# print_it(my_dict2)

