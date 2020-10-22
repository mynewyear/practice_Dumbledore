
def find_sum(nums, target):
    variants = set()
    for el in nums:
        if target - el in variants:
            return True
        else:
            variants.add(el)
    return False

print(find_sum([1, 3, 2, 12, 11], 5))
print(find_sum([1, 3, 2, 12, 11], 50))