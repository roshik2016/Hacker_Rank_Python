if __name__ == '__main__':
    n = int(input())
    count = 0
    arr = list(map(int, input().split()))
    print(sorted(set(arr),reverse=True)[1])