str = "k:1|k1:2|k2:3|k3:4"
def str2dict(str1):
    dict1 = {}
    for items in str1.split('|'):
        key, value = items.split(':')
        dict1[key] = value
    return dict1
d = {k: int(v) for t in str.split("|") for k, v in (t.split(":"), )}
print(d)