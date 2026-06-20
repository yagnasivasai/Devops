def string_reverse(string):
    reverse_string = ""
    index = len(string)
    while index > 0:
        reverse_string = reverse_string + string[index - 1]
        index = index - 1
    return reverse_string


print(string_reverse('yegnasivasai'))
