name = 'prashant*is*a*good*programmer'
newname = ''
val = ''
for i in name:
    if i !='*':
        newname += i
    else:
        val+=i
print(newname)
print(str(val+newname)) 