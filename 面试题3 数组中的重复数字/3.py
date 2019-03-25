class Solution():
    """
    思路：判断当前元素是否是数组的下标，如果数组中不含有重复元素，当前元素应该等于下标的。
    如果不等于数组下标，将元素放到当前元素值的下标位置，直到满足元素值等于下标值为止。
    如果当前元素与元素值作为下标对应的值相等，那这个元素便是重复的。
    """
    def duplicate_number(self, nums):
        if not nums or max(nums) >= len(nums) or min(nums) < 0:
            return None

        for i in range(len(nums)):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return True


if __name__ == '__main__':
    tests = [
        [],
        [2],
        [2, 1, 3, 0, 2, 2],
        [1, 2, 0],
    ]
    for i in tests:
        print(Solution().duplicate_number(i))
