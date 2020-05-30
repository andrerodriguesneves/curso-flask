a = 0
b = 7

## EAFP

try:
    b.upper()
    print(b // a)
except AttributeError as e:
    print("Nao posso transformar n em maiusculo ", str(e))
except ZeroDivisionError as e:
    print("Erro: ", str(e))
