def updated_list(items):
    if not items:
        return "No items in the list"
    else:
        formatted_string = ', '.join(items[:-1])
        formatted_string += f", and {items[-1]}"
        return formatted_string


spam = ['apples', 'bananas', 'tofu', 'cats']
result = updated_list(spam)
print(result)
