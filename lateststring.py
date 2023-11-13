def longest_string(strings):
    if not strings:
        return None  

    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string

    return longest

string_list = ["apple", "banana", "kiwi", "hippopotamus", "strawberry", "blueberry"]
longest = longest_string(string_list)
print(longest)
