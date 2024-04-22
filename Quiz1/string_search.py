def search_string_in_array(string, array):

    indices = []
    for i, item in enumerate(array):
        if string == item:
            indices.append(i)
    return indices

my_array = ["apple", "banana", "orange", "apple", "grape"]
search_string = "apple"
indices = search_string_in_array(search_string, my_array)
if indices:
    print(f"The string '{search_string}' is found at indices: {indices}")
else:
    print(f"The string '{search_string}' is not found in the array.")
