import os

# Cria a pasta do usuário dentro do diretório 'usuarios' caso ainda não exista
def criar_pasta_usuario(email):
    pasta = f"usuarios/{email}"
    if not os.path.exists(pasta):
        os.makedirs(pasta) # Criar uma pasta para cada usuário cadastrado caso não exista

# Cadastra um novo usuário e cria a pasta correspondente
def cadastrar_usuario():
    print("\n📋 Cadastro de Usuário 📋")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    if not os.path.exists("projeto/usuarios.txt"): # Se não existir a pasta usuarios.txt
        open("projeto/usuarios.txt", "w").close() # O programa retornará um novo arquivo em modo de escrita

    with open("projeto/usuarios.txt", "r") as f: # Chamando usuarios.txt de "f"
        for linha in f:
            if linha.strip().split(",")[1] == email: # Separando cada termo por ","
                print("❌ Email já cadastrado!")
                return

    with open("projeto/usuarios.txt", "a") as f: # Vai abrir o arquivo de usuarios e inserir o novo usuario cadastrado
        f.write(f"{nome},{email},{senha}\n")

    criar_pasta_usuario(email) # Chamar a função de criar pasta
    print("✅ Usuário cadastrado com sucesso!")

# Realiza o login do usuário e retorna o e-mail se for bem-sucedido
def login():
    print("\nLogin 🔐")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    with open("projeto/usuarios.txt", "r") as f: # Abrir a pasta de usuarios chamando de "f"
        for linha in f:
            nome_arquivo, email_salvo, senha_salva = linha.strip().split(",") # Armazenando email e senha do usuario
            if email == email_salvo and senha == senha_salva: # Atribuindo condição para email salvo e senha salva
                print(f"\n✅ Login realizado com sucesso. Bem-vindo(a), {nome_arquivo}!")
                return email

    print("❌ Email ou senha incorretos!") # Para caso o usuario não tenha retornado o email e a senha dos emails e senhas salvas
    return None

# Busca uma música por nome e oferece a opção de curtir após encontrar
def buscar_musica(email): # Chamando a função após o login
    nome_busca = input("\n🔎 Digite o nome da música: ").strip().lower()
    with open("projeto/musicas.txt", "r") as f: # Abrir o arquivo de musicas como formato de leitura
        for linha in f:
            nome, artista, tempo, genero = linha.strip().split(",")
            if nome_busca == nome.strip().lower(): # Se o nome da busca for igual ao do arquivo retornar:
                print(f"🎵 Música encontrada:\n  Nome: {nome}\n  Artista: {artista}\n  Duração: {tempo}\n  Gênero: {genero}")
                opcao = input("💖 Deseja curtir esta música? (s/n): ").strip().lower()
                if opcao == "s":
                    curtir_musica(email, linha.strip()) # Chamar a função de curtir musica
                return
    print("❌ Música não encontrada!") # Caso o programa não encontre a musica no arquivo

# Função que grava uma música nas curtidas e histórico do usuário
def curtir_musica(email, musica): # Chamando a função dentro de musica
    with open(f"usuarios/{email}/curtidas.txt", "a") as f:
        f.write(musica + "\n") # Vai armazenar a musica curtida dentro do arquivo "curtidas.txt"
    with open(f"usuarios/{email}/historico_curtidas.txt", "a") as f:
        f.write(musica + "\n") # Vai armazenar a curtida dentro do histórico
    print("💖 Música curtida!")

# Remove uma música da lista de curtidas e registra no histórico de descurtidas
def descurtir_musica(email): # Chamando a função após o login
    nome_musica = input("Digite o nome da música a descurtir: ").strip().lower()
    caminho = f"usuarios/{email}/curtidas.txt" # Caminho das músicas para cada usuario em "email"
    if not os.path.exists(caminho):
        print("❌ Nenhuma música curtida ainda!")
        return

    novas_musicas = [] # Atribuindo uma lista para musicas curtidas
    descurtida = False # Armazenando descurtida
    with open(caminho, "r") as f: # Abre o caminho do usuario como modo de leitura
        for linha in f:
            nome, artista, tempo, genero = linha.strip().split(",") # Separa os dados da musica
            if nome.strip().lower() != nome_musica: # Compara o nome da musica digitada com a que é exibida da lista
                novas_musicas.append(linha.strip()) # Se for diferente mantém a musica na lista
            else:
                descurtida = True
                with open(f"usuarios/{email}/historico_descurtidas.txt", "a") as hist: # Vai abrir historico de descurtidas do usuario em modo de adição
                    hist.write(linha.strip() + "\n") # Altera o arquivo com a nova musica descurtida

    if descurtida:
        with open(caminho, "w") as f: # Abre o caminho de descurtidas em modo de escrita
            for m in novas_musicas:
                f.write(m + "\n") # Reescreve cada musica no arquivo
        print("💔 Música descurtida com sucesso!")
    else:
        print("❌ Música não encontrada nas curtidas!")

# Exibe o histórico de curtidas e descurtidas
def visualizar_historico(email): # Abre histórico com o usuario logado
    while True:
        print("\n📜 Histórico")
        print("1. Ver músicas curtidas")
        print("2. Ver músicas descurtidas")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n💖 Músicas Curtidas:")
            caminho = f"usuarios/{email}/historico_curtidas.txt" # Armazena o caminho do histórico de curtidas do usuario
            if os.path.exists(caminho): # Se o caminho do historico existir...
                with open(caminho, "r") as f: # Abrir o caminho em modo de leitura
                    print(f.read()) # Retorna as musicas do caminho
            else:
                print("Nenhuma música curtida.")

        elif opcao == "2":
            print("\n💔 Músicas Descurtidas:")
            caminho = f"usuarios/{email}/historico_descurtidas.txt" # Armaezena o histórico de descurtidas do usuario
            if os.path.exists(caminho): # Se o caminho e existir...
                with open(caminho, "r") as f: # Abrir o caminho em modo de leitura
                    print(f.read()) # Retorna as musicas do caminho
            else:
                print("Nenhuma música descurtida.")

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

# Menu para gerenciar playlists (criar, excluir, acessar)
def gerenciar_playlists(email):  # Função para gerenciar playlists de um usuário específico
    while True:  # Laço para exibir o menu até o usuário escolher sair
        print("\n🎼 Gerenciar Playlists")  # Cabeçalho do menu
        print("1. Criar nova playlist")  # Opção de criar playlist
        print("2. Excluir playlist")  # Opção de excluir playlist
        print("3. Acessar playlist")  # Opção de acessar/editar playlist
        print("0. Voltar")  # Opção de sair do menu
        escolha = input("Escolha uma opção: ")  # Solicita ao usuário uma escolha

        if escolha == "1":  # Criar nova playlist
            nome = input("Digite o nome da nova playlist: ")  # Pede o nome da playlist
            caminho_lista = f"usuarios/{email}/playlists.txt"  # Caminho para o arquivo com os nomes das playlists
            with open(caminho_lista, "a") as f:  # Abre o arquivo em modo de adição
                f.write(nome + "\n")  # Adiciona o nome da nova playlist ao arquivo
            open(f"usuarios/{email}/playlist_{nome}.txt", "w").close()  # Cria um novo arquivo vazio para a playlist
            print("✅ Playlist criada com sucesso!")  # Confirmação ao usuário

        elif escolha == "2":  # Excluir playlist
            playlists = listar_playlists(email)  # Obtém a lista de playlists do usuário
            if playlists:  # Verifica se há playlists disponíveis
                print("\nPlaylists:")  # Exibe título
                for i, pl in enumerate(playlists):  # Lista todas as playlists numeradas
                    print(f"{i + 1}. {pl}")

                entrada = input("Digite o número da playlist para excluir: ")  # Solicita a escolha do usuário
                if entrada.isdigit():  # Verifica se o valor digitado é um número
                    num = int(entrada)  # Converte a entrada para inteiro
                    if 1 <= num <= len(playlists):  # Verifica se o número está dentro do intervalo válido
                        nome = playlists[num - 1]  # Recupera o nome da playlist selecionada
                        caminho = f"usuarios/{email}/playlist_{nome}.txt"  # Caminho do arquivo da playlist
                        if os.path.exists(caminho):  # Verifica se o arquivo da playlist existe
                            os.remove(caminho)  # Remove o arquivo da playlist
                        else:
                            print("⚠️ Arquivo da playlist não encontrado!")  # Aviso caso o arquivo não exista

                        playlists.pop(num - 1)  # Remove a playlist da lista em memória
                        with open(f"usuarios/{email}/playlists.txt", "w") as f:  # Abre o arquivo de listas para sobrescrever
                            for pl in playlists:
                                f.write(pl + "\n")  # Reescreve todas as playlists restantes
                        print("🗑️ Playlist excluída com sucesso!")  # Confirmação da exclusão
                    else:
                        print("❌ Número fora do intervalo válido.")  # Número fora da faixa
                else:
                    print("❌ Entrada inválida! Por favor, digite apenas o número da playlist.")  # Entrada não numérica

        elif escolha == "3":  # Acessar playlist existente
            playlists = listar_playlists(email)  # Obtém a lista de playlists
            if playlists:
                print("\nPlaylists:")  # Exibe título
                for i, pl in enumerate(playlists):  # Lista as playlists com numeração
                    print(f"{i + 1}. {pl}")
                entrada = input("Digite o número da playlist para acessar: ")  # Solicita a escolha
                if entrada.isdigit():  # Verifica se é número
                    num = int(entrada)
                    if 1 <= num <= len(playlists):  # Se está no intervalo válido
                        acessar_playlist(email, playlists[num - 1])  # Acessa a playlist selecionada
                    else:
                        print("❌ Número fora do intervalo válido.")  # Fora do intervalo
                else:
                    print("❌ Entrada inválida! Por favor, digite apenas o número da playlist.")  # Entrada inválida

        elif escolha == "0":  # Sair do menu
            break  # Encerra o laço e volta para o menu anterior

        else:
            print("❌ Opção inválida! Tente novamente.")  # Entrada fora das opções válidas

# Lista todas as playlists de um usuário
def listar_playlists(email):
    caminho = f"usuarios/{email}/playlists.txt" # Armazena o caminho das playlists
    if not os.path.exists(caminho): # Se não existir um caminho para playlits...
        print("Nenhuma playlist criada.")
        return [] # Retorna uma lista

    with open(caminho, "r") as f: # Abre o caminho da playlist no modo leitura
        playlists = [linha.strip() for linha in f if linha.strip()] # Lê as linhas da lista
    if not playlists: # Verifica se a lista está vazia
        print("Nenhuma playlist criada.") # Informa que o usuario não possuí playlists caso não tenha criado
    return playlists

# Acessa e gerencia uma playlist: adicionar ou remover músicas
def acessar_playlist(email, nome_playlist): # Acessa a playlist do usuario através do nome que o usuario criou
    caminho = f"usuarios/{email}/playlist_{nome_playlist}.txt" # Armazena o caminho da playlist
    while True:
        print(f"\n🎵 Playlist: {nome_playlist}")
        print("1. Adicionar música")
        print("2. Excluir música")
        print("3. Visualizar músicas")
        print("0. Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_busca = input("Digite o nome da música a adicionar: ").strip().lower() # Digita o nome da musica
            with open("projeto/musicas.txt", "r") as f: # Abre o arquivo de musicas no modo leitura
                for linha in f:
                    nome, artista, tempo, genero = linha.strip().split(",") # Busca informações da musica
                    if nome.strip().lower() == nome_busca: # Para caso a musica seja o mesmo da musica buscada
                        with open(caminho, "a") as pl: # Abre o caminho da playlist em modo de adição
                            pl.write(linha.strip() + "\n") # Adiciona a musica na playlist
                        print("🎶 Música adicionada à playlist!")
                        break
                else:
                    print("❌ Música não encontrada!")

        elif escolha == "2":
            nome_remover = input("Digite o nome da música a remover: ").strip().lower() # Nome da musica que será removida
            if not os.path.exists(caminho): # Verifica se o caminho da playlist existe
                print("❌ Playlist vazia ou inexistente!")
                continue # Volta ao menu
            with open(caminho, "r") as pl: # Abre o caminho da playlist no modo leitura
                linhas = pl.readlines() # Retorna as linhas que o programa vai ler
            with open(caminho, "w") as pl: # Abre a playlist como modo de escrita
                removido = False # Armazena a remoção
                for linha in linhas:
                    nome, artista, tempo, genero = linha.strip().split(",") # Extrai os dados da musica
                    if nome.strip().lower() != nome_remover: # Para caso não seja a musica desejada para remoção...
                        pl.write(linha) # O programa reescreve
                    else: # Se não...
                        removido = True # Marca a musica que será removida
                if removido: # Se removido...
                    print("🗑️ Música removida da playlist!")
                else:
                    print("❌ Música não encontrada na playlist!")

        elif escolha == "3":  # Visualizar músicas
            if not os.path.exists(caminho) or os.stat(caminho).st_size == 0: # Verifica se a playlist está vazia ou não existe
                print("📂 A playlist está vazia.")
            else:
                print("\n🎼 Músicas na playlist:")
                with open(caminho, "r") as pl: # Abre o caminho da playlist como modo de leitura
                    for linha in pl:
                        nome, artista, tempo, genero = linha.strip().split(",") # Extrai os dados da playlist
                        print(f"🎵 Nome: {nome}\n   🎤 Artista: {artista}\n   ⏱️ Tempo: {tempo}\n   🎧 Gênero: {genero}\n")
                        # Exibe o nome das musicas formatadas
        elif escolha == "0":
            break # Sai do laço e volta ao menu anterior

        else:
            print("❌ Opção inválida! Tente novamente.")

# Menu principal para o usuário logado
def menu_usuario(email): # Chama o menu do usuario através do seu email
    while True: # Cria um laço para enquanto logado
        print("\n🎧 Menu Principal")
        print("1. Buscar música")
        print("2. Descurtir música")
        print("3. Visualizar histórico")
        print("4. Gerenciar playlists")
        print("0. Deslogar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            buscar_musica(email) # Chama a função de buscar musicas no caso 1
        elif opcao == "2":
            descurtir_musica(email) # Chama a função de descurtir musicas no caso 2
        elif opcao == "3":
            visualizar_historico(email) # Chama a função de visualizar histórico no caso 3
        elif opcao == "4":
            gerenciar_playlists(email) # Chama a função de gerenciar playlist no caso 4
        elif opcao == "0":
            print("👋 Saindo do sistema...") # Sai do laço para o caso 5
            break
        else:
            print("Opção inválida!")

# Menu inicial: permite cadastro, login ou sair
def main(): # Chama o painel principal do sistema
    while True: # Cria o laço do sistema
        print("\n🎶 Bem-vindo ao Meu Spotifei 🎶")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario() # Chama a função para cadastra usuario no caso 1
        elif escolha == "2":
            usuario = login() # Chama a função de logar o usuario para o caso 2
            if usuario: # Se validar o acesso
                menu_usuario(usuario) # O programa chama a função do menu do usuario
        elif escolha == "0": # Encerra o programa e fecha o laço para o caso 3
            print("👋 Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida!")

# Execução do programa
if __name__ == "__main__":
    main()
