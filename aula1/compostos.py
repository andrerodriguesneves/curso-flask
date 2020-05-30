#.........0...........1........2

cores = ["vermelho", "verde", "azul"]
numeros = [1, 2, 3]
mistura = [1, "bruno", 4.5, True, cores, numeros, [1, 2, 32]]

cores.append('amArelo')
cores.insert(1, "branco")
cores.remove('verde')

print(cores)

# tuplas
identidade = ('Andre', '11716992710', 15)

print(f"Nome: {identidade[0]}")
print(f"CPF: {identidade[1]}")
print(f"Idade: {identidade[2]}")

# desempacotamento de tuplas
nome, cpf, idade = identidade
print(nome, cpf, idade)

# Dicionarios

pessoa = {
    "nome": "Andre",
    "cpf": "12345678912",
    "idade": 18,
    "cores_preferidas": cores,
    "numero_preferidos": numeros
}

pessoa["idade"] = 19
pessoa["canal"] = "@karlamag"

print(f"Ola {pessoa['nome']} voce tem {pessoa['idade']} anos.")



# iteração
print('########## iteração')

for cor in cores:
    print(cor.upper())

print("Andre"[0]) # primeira Letra
print("Andre"[-1]) # Ultima Letra

for letra in 'Andre':
    if letra == 'n':
        continue
    print(letra)

print('########## comprehension')
# comprehension
print([letra for letra in 'Andre'])

# comprehension filtrada
print([letra for letra in 'Andre' if letra != 'n'])

for chave in pessoa:
    print(chave," : ", pessoa[chave])

for chave, valor in pessoa.items():
    print(chave," : ", valor)