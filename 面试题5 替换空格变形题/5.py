"""
合并两个有序数组，保证合并后的数组仍是有序的
要求：
在原数组 list1 上做改变，list1 的空间足够
要点：
从后往前遍历
"""


class Solution():
    def merge_sorted_array(self, lst1, lst2):

        if not lst1:
            return lst2
        elif not lst2:
            return lst1

        l1_len = len(lst1) - 1
        l2_len = len(lst2) - 1

        i, j = l1_len, l2_len

        while lst1[i] is None:
            i -= 1
        while i >= 0 and j >= 0:
            if lst1[i] > lst2[j]:
                lst1[l1_len] = lst1[i]
                i -= 1
            else:
                lst1[l1_len] = lst2[j]
                j -= 1
            l1_len -= 1

        # 将 lst1 遍历完，但 lst2 还剩的元素拷贝到 lst1 中
        if i < 0:
            lst1[:l1_len + 1] = lst2[:j + 1]

        return lst1


if __name__ == '__main__':
    a1 = [2, 5, 6, 9]
    a2 = [1, 3, 8]
    a1.extend([None] * len(a2))
    print(Solution().merge_sorted_array(a1, a2))
