#Pythonチャレンジ1
def chunk(target, size):
    return [target[i:i + size] for i in range(0, len(target), size)]

#Pythonチャレンジ2
def dict_flatten(target, separator):
    result = {}
    for k, v in target.items():
        if isinstance(v, dict):
            for i, j in dict_flatten(v, separator).items():
                result[k + separator + i] = j
        else:
            result[k] = v

    return result

if __name__ == '__main__':
    print(dict_flatten({"foo": {"bar": "baz"}, "hoge": "fuga"}, "_"))

#Pythonチャレンジ3
def ordinal(num):
    if num % 10 == 1 and num % 100 != 11:
        return str(num) + 'st'
    elif num % 10 == 2 and num % 100 != 12:
        return str(num) + 'nd'
    elif num % 10 == 3 and num % 100 != 13:
        return str(num) + 'rd'
    else:
        return str(num) + 'th'

#Pythonチャレンジ4
ulist = list()

def unique_user(username):
    result = username not in ulist
    if result:
        ulist.append(username)
    return result


def unique_user_count():
    return len(ulist)
