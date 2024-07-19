class BreakingTheRecords:
    def breakingRecords(self, scores):
        # Write your code here
        max = scores[0]
        min = scores[0]
        max_count = 0
        min_count = 0
        for score in scores:
            if score > max:
                max = score
                max_count += 1
            if score < min:
                min = score
                min_count += 1
        return max_count, min_count