def Sum(n):
    if n == 1:
        return 1
    else:
        return n*n*n + Sum(n-1)

def main():
    n = int(input())
    print(Sum(n))
    
if __name__ == "__main__":
    main()
