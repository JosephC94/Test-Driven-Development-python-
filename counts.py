def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("Hello world") == 1, "one upper case"
assert count_upper_case("hello world") == 0, "no upper case characters"
assert count_upper_case("*&^%$ABS") == 3, "special characters"

print("all tests passed!")
