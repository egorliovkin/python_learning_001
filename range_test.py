# v1=int(input())
# v2=int(input())
# h1=int(input())
# h2=int(input())
v1=1
v2=3
h1=2
h2=4

print("\t"+"\t".join([f"{x}" for x in range(h1,h2+1)]))
for y in range(v1,v2+1):
    print(f"{y}\t"+"\t".join([f"{x*y}" for x in range(h1,h2+1)]))