def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    less = []
    greater = []
    base = nums.pop()
    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + [base] + quick_sort(greater)

def main():
    nums = [2, 5, 3, 1, 9, 0, 4, 8, 6, 7]
    print(quick_sort(nums))

main()