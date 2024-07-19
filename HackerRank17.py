class BirthDays:
    def birthday(s, d, m):
    # Write your code here
        count = 0
        for i in range(len(s)):
            if sum(s[i:i+m]) == d:
                count += 1
        return count