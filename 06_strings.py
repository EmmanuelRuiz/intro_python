text = "Estoy aprendiendo python"
#hay estos caracteres en string?
print("js" in text)
if "js" in text:
  print("está cool")
else:
  print("super cool")

#cantidad de caracteres en el string
size = len(text)
print(size)

#mayusculas
print(text.upper())
print(text.lower())
print(text.count("a"))
print(text.swapcase())
print(text.startswith("Estoy"))
print(text.endswith("rust"))
print(text.replace("python", "js"))

print(text.capitalize())
print(text.title())
print(text.isdigit())
