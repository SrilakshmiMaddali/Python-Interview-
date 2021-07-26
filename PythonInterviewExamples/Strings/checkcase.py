def isalphanum(s):
    for i in s:
        if i.isalnum():
            result = True
            break
        else:
            result = False
    return result


def isalphas(s):
    for i in s:
        if i.isalpha():
            result = True
            break
        else:
            result = False
    return result


def isdigits(s):
    for i in s:
        if i.isdigit():
            result = True
            break
        else:
            result = False
    return result


def islowercase(s):
    for i in s:
        if i.islower():
            result = True
            break
        else:
            result = False
    return result


def isuppercase(s):
    for i in s:
        if i.isupper():
            result = True
            break
        else:
            result = False
    return result


if __name__ == '__main__':
    s = input()
    if 0 < len(s) < 1000:
        print(isalphanum(s))
        print(isalphas(s))
        print(isdigits(s))
        print(islowercase(s))
        print(isuppercase(s))

