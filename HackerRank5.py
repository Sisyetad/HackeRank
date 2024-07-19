class DiagonalDifference:
    def diagonalDifference(self, arr):
        # Write your code here
        left = 0
        right = 0
        for i in range(len(arr)):
            left += arr[i][i]
            right += arr[i][len(arr) - 1 - i]
        return abs(left - right)