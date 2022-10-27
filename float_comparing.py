a=1.11-1.10
b=2.11-2.10
print(f" a = {a:>.2f} b = {b:<.2f}")
diff=abs(a-b)
if diff<=0.01:
    print("a=b")
else:
    print("a<>b")
