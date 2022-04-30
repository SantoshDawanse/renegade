
def first_non_repeating_character(word):

    arr = list(word)

    for index, i in enumerate(arr):
        new_arr = arr.copy()
        new_arr.pop(index)
        if not i in new_arr:
            return f"{i} is non repeating"
    
    return "-1"


print(first_non_repeating_character("acdacf"))
