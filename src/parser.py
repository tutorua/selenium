
def test(*args):
    print(args)
    #for i in range(len(args)):
    #    print("Index is %d argument is %s" % (i, args[i]))
    # below is used tuple enumeration and unpacking
    for i, s in enumerate(args):
        print("Parser module: Index is %d argument is %s" % (i, s))
    pass
