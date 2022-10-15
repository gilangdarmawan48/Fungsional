
# get key from dictionary value
def get_dict_key(val, my_dict: dict):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"

# handling respon
def message(msg):
    print(str(msg))