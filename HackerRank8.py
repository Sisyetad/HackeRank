class MinMaxSum:
    def miniMaxSum(self, arr):
        # Write your code here
        arr.sort()
        min = 0
        max = 0
        for i in range(len(arr) - 1):
            min += arr[i]
        for i in range(1, len(arr)):
            max += arr[i]
        print(min, max)