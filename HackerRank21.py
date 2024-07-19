class BonAppetit:
    def bonAppetit(self, bill, k, b):
        anna = 0
        for i in range(len(bill)):
            if i != k:
                anna += bill[i]
        anna = anna // 2
        if anna == b:
            print("Bon Appetit")
        else:
            print(b - anna)
            