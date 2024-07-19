class CountAppleAndOrange:
    def countApplesAndOranges(self, s, t, a, b, apples, oranges):
        # Write your code here
        count_apple = 0
        count_orange = 0
        for i in range(len(apples)):
            if a + apples[i] in range(s, t + 1):
                count_apple += 1
        for i in range(len(oranges)):
            if b + oranges[i] in range(s, t + 1):
                count_orange += 1
        print(count_apple)
        print(count_orange)
        