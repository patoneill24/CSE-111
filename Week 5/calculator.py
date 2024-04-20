def add(*nums):
    ans = 0
    for num in nums:
        ans += num
    return ans

def multiply(*nums):
    ans = 1
    for num in nums:
        ans *=num
    return ans

def main():
    print(multiply(2,10))

if __name__ == "__main__":
    main()


