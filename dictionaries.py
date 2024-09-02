d1 = {1: "Scissors", 2: "Rock", "a": "Paper", "b": "Kitchen", "d": "blank","a": "Clone" }
print(d1)
print(d1["a"])
print(d1["b"])
print(len(d1))
print(type(d1))
print(d1.get("geo","Unknown"))
d1[4] = "good"
print(d1[4])
print(d1)
print(d1.keys())
print(d1.values())
print("d" in d1)
print("n" in d1)
del d1["b"]
print(d1)
d1[2] = "Bigger_rock"
print(d1)
empty = []
for i in d1:
    empty.append(i)
print(empty)
