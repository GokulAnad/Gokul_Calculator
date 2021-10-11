class Sum:
    def __init__(self, a, b):
        num1 = int(a)
        num2 = int(b)
        result = num1 + num2
        # return result
        print(result)

    def display(self):
        print("hai")

f = open("sample2.py","r")
print(f.read())
f.close()
s = Sum(20, 30)

s.display()
