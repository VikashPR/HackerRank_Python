if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    arr2 = set(arr)
    arr2.remove(max(arr2))
    print(max(arr2))
