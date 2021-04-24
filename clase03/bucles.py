#for <var> in <iterable>:
#   <instructions>
for x in [1, 3, 4]:
    print (x)

valores= {'A': 4, 'B': 5, 'C':6}
for k in valores:
    #imprime los keys
    print(k)
for v in valores.values():
    #imprime los values
    print(v)
for k,v in valores.items():
    #print key and value
    print('k=',k, "v=", v)