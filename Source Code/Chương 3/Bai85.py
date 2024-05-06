def main():
    n = int(input())
    if n >= 1 and n <= 3:
        print("Tháng",n,"thuộc quý I")
    elif n >= 4 and n <= 6:
        print("Tháng",n,"thuộc quý II")
    elif n >= 7 and n <= 9:
        print("Tháng",n,"thuộc quý III")
    else:
        print("Tháng", n, "thuộc quý IV")

if __name__ == "__main__":
    main()
