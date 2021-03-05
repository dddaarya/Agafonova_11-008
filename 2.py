def no_dub(my_dict):
    new_dict = {}
    values = []
    for k, v in my_dict.items():
        if not (v in values):
            new_dict[k] = v
            values.append(v)
    return new_dict
