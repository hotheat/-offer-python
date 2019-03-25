class Solution():
    def duplicate_number(self, nums, length):
        if not nums or max(nums) > length or min(nums) < 1:
            return False

        start, end = 1, len(nums) - 1
        while end >= start:
            mid = (start + end) // 2
            count = self.count_range(nums, start, mid)
            if start == end:
                if count > 1:
                    return start
                else:
                    break
            if count > (mid - start + 1):
                end = mid
            else:
                start = mid + 1
        return True

    def count_range(self, nums, start, mid):
        count = 0

        for i in nums:
            if start <= i <= mid:
                count += 1
        return count


if __name__ == '__main__':
    tests = [
        [],
        [1],
        [2, 1, 3, 2, 2, 4, 4],
        [2, 1, 3, 4, 4],
        [1, 2, 3, 4],
    ]
    for i in tests:
        print(Solution().duplicate_number(i, len(i)))
