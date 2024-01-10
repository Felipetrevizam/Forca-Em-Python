while True:

    palavra_secreta = input("Insira a palavra secreta: ").lower()
    tentativa = 0
    num_asterisco = len(palavra_secreta)
    palavra_descoberta = ['*' for letrinha in palavra_secreta]

    print("\nAgora tente adivinhar a palavra secreta")

    while num_asterisco > 0:
        letra = input("\nInsira uma letra: ").lower()
        tentativa += 1

        if letra in palavra_secreta:
            for i, letras in enumerate(palavra_secreta):
                if letras == letra:
                    palavra_descoberta[i] = letra

            num_asterisco = palavra_descoberta.count('*')
            print(' '.join(palavra_descoberta))

        else:
            print("\nLetra não encontrada, tente novamente.\n")

    print(f"\nVocê encontrou a palavra secreta: {palavra_secreta}\nVocê precisou de {tentativa} tentativas.")

    comando = 1
    while comando == 1:
        pergunta = input(f"\nDeseja jogar novamente? (Digite Y/N) \n")
        if pergunta == 'Y' or pergunta == 'y':
            break
            print("\n\n")
        elif pergunta == 'N' or pergunta == 'n':
            exit()
        else:
            print("Comando invalido")
            continue
