abc = [232, 123, 'sadas', 123]
d = {'Michael': 95, 'Bob': 75, "Tracy": 84, "abc": abc}

print(d['Michael'])
print(d['abc'])
c = d.copy()
print(c)
d.clear()
print(d)
e = c.get("abc")
print(e)
