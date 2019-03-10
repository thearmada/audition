d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
result = sorted(d.items(), key=lambda x: x[1])
print(result)