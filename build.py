def build(string, k):
    if string is None:
        return False
    if k is None:
        return False
    low_index = 0
    max_length = 0
    chars_to_index_map = {}
    for index, char in enumerate(string):
        chars_to_index_map[char] = index
        if len(chars_to_index_map) > k:
            low_index = min(chars_to_index_map.values())
            del chars_to_index_map[string[low_index]]
            low_index += 1
        max_length = max(max_length, index - low_index + 1)
    return max_length

value= build("hello","rgerge")
print(value)