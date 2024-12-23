from
def adicionar_contatos(contatos, nome, telefone, email):
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print(f"\nContato adicionado: {nome}")
  return

def visualizar_contatos(contatos):
  print("Contatos: ")
  for indice, contato in enumerate(contatos):
    favorito_done = contato["favorito"]
    indice += 1
    favorito = "★" if favorito_done else " "
    valor_nome = contato["nome"]
    valor_telefone = contato["telefone"]
    valor_email = contato["email"]
    print(f"\n {indice}. [{favorito}] Nome: {valor_nome}. Telefone:  {valor_telefone}. E-mail: {valor_email} ")
    return

contatos = []

while True:
  print("\n Menu da lista de contatos.")
  print("1. Adicionar contato.")
  print("2. Ver contato.")
  print("3. Editar contato.")
  print("4. Marcar/desmarcar um contato como favorito.")
  print("5. Ver contato favoritos.")
  print("6. Apagar contato.")
  print("7. Sair")

  escolha = str(input("Escolha uma opção da lista de Contatos: "))

  if escolha == "1":
    print("\nCriando contato.")
    nome_contato = str(input("\nAdicione o nome do contato: "))
    telefone_contato = str(input("\nAdicione o telefone do contato: "))
    email_contato = str(input("\nAdicione o email do contato: "))
    adicionar_contatos(contatos, nome_contato, telefone_contato, email_contato)
  elif escolha == "2":
    print("\n Lista de contatos.")
    visualizar_contatos(contatos)
  elif escolha == "7":
    print("\n Saindo da lista de contatos...")
    break
  else: 
    print("\nOpção incorreta.")