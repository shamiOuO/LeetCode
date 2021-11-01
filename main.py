def twoSum(nums, target):
    array = {}
    for index, numbers in enumerate(nums):
        if(target - numbers) in array:
            print(array)
            print([array[target-numbers], index])
            return [array[target-numbers], index]
        array[numbers] = index


twoSum(nums=[2, 7, 11, 15], target=22)
