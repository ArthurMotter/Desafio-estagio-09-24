def contar_letra_a(texto):
#logica para achar a letra A
  texto = texto.lower()
  contagem = texto.count('a')
  return contagem > 0, contagem

# Entrada de dados 
texto = input("Digite uma string: ")

# Processamento e saída de dados
tem_a, quantidade = contar_letra_a(texto)

if tem_a:
  print(f"A string contém a letra 'a' {quantidade} vezes.")
else:
  print("A string não contém a letra 'a'.")