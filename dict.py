person = {"namn": "Ahmad", "ålder": 17, "stad": "halmstad"}
print(person)

fruits = {"apple": 10, "banana": 5, "orange": 8}
print(fruits["apple"])

fruits["pear"] = 7
print(fruits)

del fruits["banana"]
print(fruits)

for k, v in fruits.items():
    print(f"{k}: {v}")

text = "python är roligt och python är populärt"
dict = {}
for ord in text.split():
    if ord in dict:
        dict[ord] += 1
    else:
        dict[ord] = 1
print(dict)

d = {"a": 1, "b": 2, "c": 3}
d_ny = {}
for k, v in d.items():
    d_ny[v] = k
print(d_ny)

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
c = {}
for k, v in a.items():
    c[k] = v
for k, v in b.items():
    c[k] = v
print(c)

data = [("Anna", "Stockholm"), ("Olle", "Göteborg"), ("Lisa", "Stockholm"), ("Per", "Malmö")]
data_ny = {}
for k, v in data:
    if k in data:
        data_ny[k] += v
    else:
        data_ny[k] = v