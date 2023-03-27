import math

# //literally just started learning python this is extremely disorienting

alist = ["bruh", 23, "bruh", "what thehell", list, 3.4]  # HOW
print(alist)

testvar = math.sqrt(4.)
print(testvar)

for x in alist:
    if type(x) == str:  # can be replaced by isinstance(x, str)
        print("is string")
    else:
        print("not string :-)")

    # str object acts as array of chars; ex:
aString = "theres no way"
print(aString[3])
print(aString[1:9])

atuple = (3, 2, "5", object, 'a', 3.2, (3, 2, 5))
for x in enumerate(atuple):
    print(x)
