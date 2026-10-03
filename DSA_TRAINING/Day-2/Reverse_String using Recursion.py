def reverse(string): # 'python'
    if len(string) <= 1: # 6<=1
        return string
    return string[len(string)-1] + reverse(string[0:len(string)-1]) # 0:3
             # n
print(reverse('python')) # 'nohtyp'
# python
# 012345 