spiska = ['17', 8, [2, 3], None, None, 'None', 13]
func1 = lambda x: x if x is not None else -1
func2 = lambda x: x if isinstance(x, str) else str(x)
spis1 = spiska
spis2 =[]
for i in spis1:
    spis2.append(func2(func1(i)))
print(spis2)
