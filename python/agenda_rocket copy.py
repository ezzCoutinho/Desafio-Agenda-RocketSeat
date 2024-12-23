from validate_email import validate_email

def valida_contato(nome, telefone, email):
  if len(nome) < 4:
    print("\nO nome tem que conter ao menos 4 dígitos.")
    return False
  elif len(telefone) < 8:
    print("\nTelefone tem que conter ao menos 8 dígitos.")
    return False
  elif not validate_email(email):
    print("\nEste e-mail é inválido.")
    return False
  return True

def adicionar_contatos(contatos, nome, telefone, email):
  if not valida_contato(nome, telefone, email):
    print("\nCONTATO NÃO SALVO.") 
  else:
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"\nContato adicionado: {nome}")
    return

def visualizar_contatos(contatos):
  for indice, contato in enumerate(contatos):
    favorito_done = contato["favorito"]
    indice += 1
    favorito = "★" if favorito_done else " "
    valor_nome = contato["nome"]
    valor_telefone = contato["telefone"]
    valor_email = contato["email"]
    print(f"\n {indice}. [{favorito}] Nome: {valor_nome}. Telefone: {valor_telefone}. E-mail: {valor_email}.")
  return

def editar_contatos(contatos, indice_contato, nome, telefone, email):
  indice_ajustado = indice_contato -1
  if indice_ajustado >= 0 and indice_ajustado <= len(contatos):
    contatos[indice_ajustado]["nome"] = nome
    contatos[indice_ajustado]["telefone"] = telefone
    contatos[indice_ajustado]["email"] = email 
    print(f"\nContato {indice_contato} foi atualizado para: \nNome: {nome}. \nTelefone: {telefone}. \nE-mail: {email}.")
    return
  else:
    print("\n Índice inválido.")

def deletar_contatos(contatos, indice_contato):
  indice_ajustado = indice_contato -1 
  if indice_ajustado >= 0 and indice_ajustado <= len(contatos):
    del contatos[indice_ajustado]
  print("\nContato foi apagado!")
  return

def marcar_favorito(contatos, indice_contato):
  indice_ajustado = indice_contato -1
  contatos[indice_ajustado]["favorito"] = True
  print(f"\nContato {indice_contato} foi favoritado!")
  return

def desmarcar_favorito(contatos, indice_contato):
  indice_ajustado = indice_contato -1
  if contatos[indice_ajustado]["favorito"]:
    contatos[indice_ajustado]["favorito"] = False
    print(f"\n Contato {indice_contato} foi desmarcado como favorito")
  elif not contatos[indice_ajustado]["favorito"]:
    print(f"\n Este contato não é favorito.")
  else:
    print(f"\n Este contato não existe.")

def contatos_favoritos(contatos):
  for indice, contato in enumerate(contatos):
    favorito = "★"
    valor_nome = contato["nome"]
    valor_telefone = contato["telefone"]
    valor_email = contato["email"]
    if contatos[indice]["favorito"]:
      indice += 1
      print(f"\n {indice}. [{favorito}] Nome: {valor_nome}. Telefone: {valor_telefone}. E-mail: {valor_email}.")
  return

contatos = []

while True:
  print("\n Menu da lista de contatos.")
  print("1. Adicionar contatos.")
  print("2. Ver contatos.")
  print("3. Editar contatos.")
  print("4. Marcar/desmarcar um contato como favorito.")
  print("5. Ver contatos favoritos.")
  print("6. Apagar contatos.")
  print("7. Sair")

  escolha = str(input("Escolha uma opção da lista de Contatos: "))

  if escolha == "1":
    print("\nCriando contato.")
    nome_contato = str(input("\n*OBRIGATÓRIO* Adicione o nome do contato: "))
    telefone_contato = str(input("\n*OBRIGATÓRIO* Adicione o telefone do contato: "))
    email_contato = str(input("\n*OBRIGATÓRIO* Adicione o email do contato: "))
    adicionar_contatos(contatos, nome_contato, telefone_contato, email_contato)
  elif escolha == "2":
    print("\n Lista de contatos: ")
    visualizar_contatos(contatos)
  elif escolha == "3":
    visualizar_contatos(contatos)
    indice_a_editar = int(input("\nEscolha o contato a ser editado: "))
    nome_a_editar = str(input("\nEdite o nome: "))
    telefone_a_editar = str(input("\nEdite o telefone: "))
    email_a_editar = str(input("\nEmail a editar: "))
    editar_contatos(contatos, indice_a_editar, nome_a_editar, telefone_a_editar, email_a_editar)
  elif escolha == "4":
    escolha_md = input("\n Para marcar um contato como favorito: 1. \n Para desmarcar um contato como favorito: 2. \n Selecione 1 ou 2: ")
    if escolha_md == "1":
      visualizar_contatos(contatos)
      indice_a_favoritar = int(input("\nMarcar um contato como favorito: "))
      marcar_favorito(contatos, indice_a_favoritar)
    elif escolha_md == "2":
      visualizar_contatos(contatos)
      indice_a_desfavorecer = int(input("\nDesmarcar um contato como favorito: "))
      desmarcar_favorito(contatos, indice_a_desfavorecer)
    else:
      print("\n Esta opção não existe!")
  elif escolha == "5":
    print("\nContatos favoritos: ")
    contatos_favoritos(contatos)
  elif escolha == "6":
    visualizar_contatos(contatos)
    indice_a_apagar = int(input("\nEscolha o contato que deseja apagar: "))
    deletar_contatos(contatos, indice_a_apagar)
  elif escolha == "7":
    print("\n Saindo da lista de contatos...")
    break
  else: 
    print("\nOpção incorreta.")