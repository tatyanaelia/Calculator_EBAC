nome="tatyana elia"
print(nome)
nome + nome
lista=[0,2,"tatyana",3]
if "t" in nome:
    print("true")
else:
    print("false")

# Solicita o nome do usuário e o exibe
nome_usuario = input("Por favor, insira seu nome: ")
print("Olá, {nome_usuario}! Bem-vindo ao nosso sistema.")

# Solicita a idade do usuário e converte para inteiro
idade_usuario = int(input("Por favor, insira sua idade: "))

# Verifica se o usuário é maior de idade
if idade_usuario >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Utilize o comando 'input' para receber ao menos 2 números de entrada do usuário;

cpf_usuario = int(input('Seu CPF: '))
print('certo')
telefone_usuario = int(input('Seu contato: '))
salario_usuario = float(input('Informe seu rendimento: '))
print('obrigada!')

# Implemente ao menos 4 operações matemáticas em seu código;
vt = int(20)
vr = int(30)
soma = vt + vr
subtracao = vt - vr
multiplicacao = vt * vr

print(f"A soma de {vt} e {vr} é: {soma}")
print(f"A subtração de {vt} menos {vr} é: {subtracao}")
print(f"A multiplicação de {vt} por {vr} é: {multiplicacao}")

#Laço de repetição, looping ou condicional
# Números fixos atribuídos no código
numero1 = 20
numero2 = 5

# Loop para permitir várias operações
while True:
    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    # Escolha do usuário
    escolha = input("Digite o número da operação desejada: ")

    if escolha == '1':
        resultado = numero1 + numero2
        print(f"A soma de {numero1} e {numero2} é: {resultado}")
    elif escolha == '2':
        resultado = numero1 - numero2
        print(f"A subtração de {numero1} menos {numero2} é: {resultado}")
    elif escolha == '3':
        resultado = numero1 * numero2
        print(f"A multiplicação de {numero1} por {numero2} é: {resultado}")
    elif escolha == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"A divisão de {numero1} por {numero2} é: {resultado:.2f}")
        else:
            print("Erro: divisão por zero não é permitida.")
    elif escolha == '5':
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")