def checkMark(a,b):
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return True
    else:
        return False

def main():
    a, b = map(int, input().split(" "))
    if checkMark(a,b):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()