print("YES" if sum(a := input())[:len(a)//2] == sum(a[len(a)//2:]) else "NO")