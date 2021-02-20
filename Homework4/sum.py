nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6
def twoSum(x, y):
    index_map = {}
    for index, num in enumerate(x):
        if y - num in index_map:
            return index_map[y - num], index
        index_map[num] = index
print(twoSum(nums1,target1))
print(twoSum(nums2,target2))
print(twoSum(nums3,target3))