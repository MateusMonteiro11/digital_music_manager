🎵 Digital Music Manager

📘 Descrição

O Digital Music Manager, apelidado de Meu Spotifei, é um sistema
interativo desenvolvido em Python que simula um gerenciador de músicas
com funcionalidades inspiradas em plataformas de streaming.

O programa permite cadastro e login de usuários, busca de músicas,
curtidas/descurtidas, gerenciamento de playlists personalizadas e
histórico de atividades, tudo armazenado localmente em arquivos de
texto.

------------------------------------------------------------------------

🧩 Estrutura do Projeto

    digital_music_manager/
    ├── projeto/
    │   ├── main.py                # Código principal do sistema
    │   ├── musicas.txt            # Banco de músicas disponíveis
    │   ├── usuarios.txt           # Registro de usuários cadastrados
    │
    └── usuarios/                  # Diretório com dados individuais dos usuários
        ├── <email_do_usuario>/    # Pasta criada automaticamente após o cadastro
        │   ├── curtidas.txt
        │   ├── historico_curtidas.txt
        │   ├── historico_descurtidas.txt
        │   ├── playlists.txt
        │   ├── playlist_<nome>.txt

------------------------------------------------------------------------

⚙️ Funcionalidades Principais

👤 Sistema de Usuários

-   Cadastro com nome, e-mail e senha, armazenados em usuarios.txt.
-   Login com validação de credenciais.
-   Criação automática de uma pasta pessoal em /usuarios/<email>/.

🎧 Músicas

-   As músicas são carregadas de musicas.txt, contendo:

        Nome, Artista, Duração, Gênero

💖 Curtidas e Descurtidas

-   Usuário pode curtir músicas após a busca, armazenando em
    curtidas.txt.
-   Ao descurtir, a música é removida da lista e registrada em
    historico_descurtidas.txt.
-   Todo o histórico é mantido separadamente por usuário.

📜 Histórico

-   Consulta das músicas curtidas e descurtidas com visualização
    completa.

🎼 Playlists Personalizadas

-   Criação, exclusão e visualização de playlists.
-   Cada playlist é armazenada como um arquivo playlist_<nome>.txt
    dentro da pasta do usuário.
-   As playlists podem receber músicas buscadas da base (musicas.txt).

------------------------------------------------------------------------

🚀 Como Executar o Projeto

1️⃣ Pré-requisitos

-   Python 3.8+ instalado no sistema.
-   Sistema operacional compatível (Windows, macOS ou Linux).

2️⃣ Clonando o repositório

    git clone https://github.com/MateusMonteiro11/digital_music_manager.git
    cd digital_music_manager/projeto

3️⃣ Executando o programa

    python main.py

4️⃣ Navegando pelo sistema

Ao iniciar, o terminal exibirá o menu principal:

    🎶 Bem-vindo ao Meu Spotifei 🎶
    1. Cadastrar usuário
    2. Login
    0. Sair

Após o login, o menu do usuário oferece:

    🎧 Menu Principal
    1. Buscar música
    2. Descurtir música
    3. Visualizar histórico
    4. Gerenciar playlists
    0. Deslogar

------------------------------------------------------------------------

💡 Exemplo de Uso

Cadastro e Login

1.  Selecione 1 - Cadastrar usuário
2.  Insira nome, e-mail e senha
3.  Após o cadastro, entre com 2 - Login

Buscando e Curtindo uma Música

1.  Escolha 1 - Buscar música
2.  Digite o nome da música, por exemplo: Shape of You
3.  Confirme a curtida digitando s

Criando uma Playlist

1.  Escolha 4 - Gerenciar playlists
2.  Crie uma nova playlist digitando o nome desejado
3.  Adicione músicas buscadas da base

------------------------------------------------------------------------

🗃️ Armazenamento de Dados

Todos os dados são armazenados em arquivos de texto, simulando um
pequeno banco de dados local.

  Arquivo                     Função
  --------------------------- -----------------------------------------------
  usuarios.txt                Registra nome, e-mail e senha de cada usuário
  musicas.txt                 Catálogo global de músicas disponíveis
  curtidas.txt                Músicas curtidas por um usuário
  historico_curtidas.txt      Histórico completo de curtidas
  historico_descurtidas.txt   Histórico completo de descurtidas
  playlists.txt               Lista de playlists criadas
  playlist_<nome>.txt         Músicas pertencentes a cada playlist

------------------------------------------------------------------------

🧠 Estrutura Lógica do Código

O sistema é dividido em funções independentes para modularidade:

  -----------------------------------------------------------------------
  Função                       Descrição
  ---------------------------- ------------------------------------------
  criar_pasta_usuario()        Cria diretório para novos usuários

  cadastrar_usuario()          Registra usuários e valida e-mails

  login()                      Realiza autenticação

  buscar_musica()              Pesquisa músicas na base

  curtir_musica() /            Gerencia curtidas e descurtidas
  descurtir_musica()           

  visualizar_historico()       Exibe histórico de interações

  gerenciar_playlists()        Cria e remove playlists

  acessar_playlist()           Permite adicionar/remover músicas em uma
                               playlist

  menu_usuario()               Exibe menu após login

  main()                       Controla o fluxo principal do programa
  -----------------------------------------------------------------------

------------------------------------------------------------------------

🔒 Segurança e Estrutura

-   Cada usuário possui sua própria pasta isolada, impedindo
    interferência em dados alheios.
-   Nenhuma dependência externa é necessária — o projeto usa apenas
    bibliotecas nativas do Python (os).

------------------------------------------------------------------------


👨‍💻 Autor

Desenvolvido por Mateus Monteiro
📧 mateusinaciomonteiro519@gmail.com
