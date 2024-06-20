def altera_texto(texto):
    texto_alterado = ''
    for i in range(len(texto)):
        if i % 2 == 0:  # posição par
            texto_alterado += texto[i].upper()
        else:
            texto_alterado += texto[i].lower()

    return texto_alterado

# Solicita ao usuário que insira um texto
texto_original = input("Insira o texto que deseja alterar: ")

# Aplica a função e exibe o resultado
texto_modificado = altera_texto(texto_original)
print("Original: ", texto_original)
print("Modificado: ", texto_modificado)
print("Trocado: ", )