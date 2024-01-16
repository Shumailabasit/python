a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = "Hello World!"
print(a[0:7])
c=" hello class "
#if "class" not in c:
  #  print("welcome class")

#else:
 #   print("bye Class")
print(c.upper())
print(c.lower())
print(c.strip())
print(c.replace("c","s"))
a = "Hello World!"
print(a.split(" \ "))
print(c+a)
print(c+" "+a)
age = "36"
txt = "My name is John, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
a,b,c=35,638,56
d=("the price is{2} strock{0}")
print(d.format(a,c,b))
txt = "We are the so-called\b  \"Vikings\" \n from the north."
print(txt)
