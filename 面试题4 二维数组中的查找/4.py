class Solution():
    """
    思路：分治法
    从右上角元素开始判断，如果右上角元素大于指定值，那么删除该列；
    如果小于指定值，删除该行，
    如果等于指定值，返回该值。
    """

    def find_element_matrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col > 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


if __name__ == '__main__':
    matrix = [
        [],
        [[1, 2], [3, 4]],
        [[1, 3], [2, 5]],
    ]

    for i in matrix:
        print(Solution().find_element_matrix(i, 4))