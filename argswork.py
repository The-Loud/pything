def myfunc(*args):
    mystr = args.split()
    count = 0
    for i in args:
        if count % 2 == 0:
            mystr.append(args[count].upper())
            count += 1
        else:
            mystr.apped(args[count].lower())
            count += 1
        print(count)
    return mystr


print(myfunc('this is a string'))
