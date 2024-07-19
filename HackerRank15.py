class GetTotalX:
    def getTotalX(self, a, b):
        # Write your code here
        count = 0
        for i in range(max(a), min(b)+1):
            if all(i % j == 0 for j in a) and all(j % i == 0 for j in b):
                count += 1
        return count