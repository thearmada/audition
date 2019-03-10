alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 100}, {'name': 'c', 'age': 99}]
def sort_by_age(list):
    return sorted(alist, key=lambda x: x['age'], reverse=True)

if __name__=='__main__':
    list2 = sort_by_age(alist)
    print(list2)