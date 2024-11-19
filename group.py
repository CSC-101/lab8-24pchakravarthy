def groups_of_3(nums : list[int]) -> list[list[int]]:
    numLists = int(len(nums) / 3)
    remainder = len(nums) % 3
    newList = []
    for i in range(numLists):
        newList.append([nums[3*i], nums[3*i+1], nums[3*i+2]])
    remainderList = []
    for i in range(remainder):
        remainderList.append(nums[3 * numLists + i])
    if remainder != 0:
        newList.append(remainderList)
    return newList