class Solution:
    def dailyTemperatures(self, temp):
        stack ={}
        output =[0]* len(temp)
        for i in range(len(temp)):
            if not stack:
                stack[temp[i]] = [i]
            else:
                j = 0
                while j < len(stack):
                    if list(stack)[j]< temp[i]:
                        for k in stack[list(stack)[j]]:
                            output[k] = i-k
                        stack.pop(list(stack)[j])
                    else:
                        j+=1
                if temp[i]in stack:
                    stack[temp[i]].append(i)
                else:
                    stack[temp[i]] = [i]
        return output
                
            
            
        
        



temperatures = [73,74,75,71,69,72,76,73]
obj = Solution()
print(obj.dailyTemperatures(temperatures))