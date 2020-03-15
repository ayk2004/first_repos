a = [2, None, 17, 5, None]
func = lambda x: 0 if x == None else x
for i in a:
    print(func(i))
