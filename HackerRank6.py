class PlusMinus:
    def plusMinus(self, arr):
        # Write your code here
        positive = 0
        negative = 0
        zero = 0
        for i in arr:
            if i > 0:
                positive += 1
            elif i < 0:
                negative += 1
            else:
                zero += 1
        print(positive / len(arr))
        print(negative / len(arr))
        print(zero / len(arr))