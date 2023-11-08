""" Pretty printing functions """


def pretty_print_dict(dic, level=1):
    for key in dic:
        print(key, " ->", end="\n" + "\t" * level)
        value = dic[key]
        if isinstance(value, dict):
            pretty_print_dict(value, level=level + 1)
        elif isinstance(value, (list, tuple)):  #  Can't use sequence as str
            print(*value, sep="\n" + "\t" * level)
        else:
            print(value)

        print()
