class DivisibleSumPairs:
    def divisibleSumPairs(self, n, k, a):
        count = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if (a[i] + a[j]) % k == 0:
                    count += 1
        return count