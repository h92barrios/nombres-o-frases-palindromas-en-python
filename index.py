""" palabra palindromas """

def reverse_str(text: str):
    new_text = ""
    for i in range( 1, len(text) + 1 ) :
        new_text += text[-i]

    t = "La palabra o frase"
    if new_text in text:
        print(
            f"{t} {text} es un palindromo.")
    else:
        print(
            f"{t} {text} no es un palindromo.")


def phrase_str(text: list):
    new_text = ''.join(text)
    reverse_str(new_text)


def divide_space(text: str):
    list_text = text.split(" ")
    num = len(list_text)
    if num >= 1:
        for i in range(num):
            reverse_str(list_text[i])
        phrase_str(list_text)
    else:
        reverse_str(list_text[0])


name = str
name = input("Ingresa tu nombre:\n")

print(
    f"Hola {name} por ahora lo que puedo hacer es comprobar palabra palindromas.")


option = str
option = input("Escribe Y para continuar o N para salir. Luego la tecla Enter:\n")
print(
    f"Oprimiste: {option}")

if option.lower() == "y":
    phrase = str
    phrase = input("Continuemos dime la palabra o frase:\n")
    divide_space(phrase)
else:
    print("adios")