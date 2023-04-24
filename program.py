import re

def validar_email(email):

    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(regex, email):
        return "E-mail válido!"
    else:
        return "E-mail inválido!"

mail = input("Digite o e-mail: ")

print( validar_email(mail))