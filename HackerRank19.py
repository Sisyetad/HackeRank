class MigratoryBirds:
    def migratoryBirds(self, arr):
        # Write your code here
        count = [0, 0, 0, 0, 0]
        for i in arr:
            count[i - 1] += 1
        return count.index(max(count)) + 1