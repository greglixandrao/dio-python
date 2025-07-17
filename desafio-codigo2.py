# Dicionário com os valores de desconto
email = input().strip()

# TODO: Verifique as regras do e-mail:
if ' ' in email or email.startswith('@'):
    print("E-mail inválido")
elif '@' not in email or email.count('@') > 1:
    print("E-mail inválido")
elif '.' not in email.split('@')[1]:
    print("E-mail inválido")
else:
    print("E-mail válido")
