txt = "Hello World"
x = txt[0]
print (x)



txt = "Hello World"
x = txt[2:5]
print(x)


txt = " Hello World "
x = txt.strip()
print(x)

txt = "Hello World"
x = txt.upper()
print(x)

txt = "Hello World"
txt = txt.lower()
print(txt)

txt = "Hello World"
txt = txt.replace("H", "J")


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))