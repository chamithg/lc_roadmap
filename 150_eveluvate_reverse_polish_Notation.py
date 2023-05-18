class Solution:
    def evalRPN(self, tokens):
        numStack = []
        
        for i in tokens:
            if i!="+" and i!="-" and i!="*" and i!="/":
                numStack.append(int(i))
            else:
                second = numStack.pop()
                first = numStack.pop()
                if i == "+":
                    numStack.append(first + second)
                elif i == "-":
                    numStack.append(first - second)
                elif i == "*":
                    numStack.append(first * second)
                elif i == "/":
                    numStack.append(math.trunc(first / second))
        
        return numStack[0]
        
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]        
obj = Solution()
print(obj.evalRPN(tokens))