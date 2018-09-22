if __name__ == '__main__':
    N = int(input())
    final_list = []
    for i in range(N):
        A = input()
        a = list(A.split(" "))
        if a[0] == "insert":
            final_list.insert(int(a[1]),int(a[2]))
        elif a[0] == "remove":
            final_list.remove(int(a[1]))
        elif a[0] == "append":
            final_list.append(int(a[1]))
        elif a[0] == "sort":
            final_list.sort()
        elif a[0] == "print":
            print(final_list)
        elif a[0] == "reverse":
            final_list.reverse()
        elif a[0] == "pop":
            final_list.pop()