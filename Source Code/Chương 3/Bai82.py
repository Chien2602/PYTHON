def maxNumber(a,b):
    if a > b:
        return a
    else:
        return b

def main():
    a, b, c = map(int, input().split())
    print(maxNumber(maxNumber(a,b), c))

if __name__ == "__main__":
    main()

