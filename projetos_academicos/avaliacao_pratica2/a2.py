def linhas():
    print("-" * 48)

linhas()
print("Maior número entre três valores (sem operadores)".center(48))
linhas()

def obter_numero(valor) -> int:
    while True:
        try:
            return int(input(valor))
        except ValueError:
            print("Erro. Digite um número inteiro válido.")

valor1 = obter_numero("Primeiro valor: ")
valor2 = obter_numero("Segundo valor: ")
valor3 = obter_numero("Terceiro valor: ")
maior_valor = max(valor1, valor2, valor3)

linhas()
print(f"O maior valor entre {valor1}, {valor2} e {valor3} é: {maior_valor}.")