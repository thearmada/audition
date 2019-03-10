#{key:value for (key, value) in iterable}字典推导
lst = [1, 2, 3, 4, 5]
res = {i: 'python'+str(i)+'期' for i in lst if i > 0}
print(res)