def Solve(a,b):
    if b == 0:
        return 0
    else:
        return -b/a

def main():
    a, b = map(int, input().split())
    print(Solve(a,b))

if __name__ == "__main__":
    main()
