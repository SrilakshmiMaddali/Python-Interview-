def split_and_join(line):
    mylist = line.split()
    return '-'.join(mylist)


if __name__=="__main__":
    s=input()
    result = split_and_join(s)
    print(result)