# YouTube e Spotify Video Downloader

Este projeto permite que você baixe vídeos e faixas de áudio de playlists do **YouTube** e **Spotify**. Através de uma interface gráfica simples feita em **Tkinter**, você pode inserir o link de uma playlist do Spotify ou do YouTube, escolher a pasta de destino e fazer o download em formato **MP4**.

## Funcionalidades

- **Baixar vídeos do YouTube**: Insira o link do vídeo e baixe no formato **MP4**.
- **Baixar faixas do Spotify**: Insira o link de uma playlist do Spotify e baixe as faixas em vídeo de alta qualidade, convertendo-as para **MP4**.
- **Interface Gráfica (GUI)**: Interface gráfica com a biblioteca **Tkinter** para facilitar a interação com o usuário.
- **Barra de progresso**: Acompanhe o progresso do download diretamente na interface.

## Tecnologias

Este projeto foi desenvolvido utilizando a linguagem **Python**. As bibliotecas principais utilizadas são:

### Bibliotecas

- **yt-dlp**: Biblioteca de código aberto para download de vídeos e áudio de várias plataformas, incluindo YouTube e outras.
- **spotipy**: Biblioteca Python para interagir com a API do Spotify e acessar informações sobre playlists, faixas, álbuns e artistas.
- **tkinter**: Biblioteca para criação de interfaces gráficas (GUI) simples, usada para facilitar a interação com o usuário.
- **ffmpeg**: Usado para a conversão de formatos de vídeo e áudio. Necessário para o correto funcionamento da aplicação.

## Pré-requisitos

Certifique-se de ter as dependências abaixo instaladas no seu sistema:

- **Python 3.x**
- **yt-dlp**: Para baixar vídeos e faixas.
- **spotipy**: Para acessar a API do Spotify e obter informações de playlists.
- **FFmpeg**: Necessário para a conversão e manipulação de vídeos. Certifique-se de instalar e configurar o **FFmpeg** no seu sistema.

## Instalação

1. **Clone este repositório para o seu computador:**

   ```bash
   git clone https://github.com/ViniLF/VideoMusic-Downloader.git
2. **Acesse a pasta do repositório clonado**<br>
No terminal, utilize o comando cd para entrar na pasta do projeto:
    ```bash
    cd VideoMusic-Downloader
3. **Instale as dependências necessárias**
    ```bash
    pip install -r requirements.txt
4. **Instalando o FFmpeg**<br>
O FFmpeg é uma ferramenta necessária para manipulação de áudio e vídeo. Caso ele não esteja instalado no seu sistema, siga as instruções abaixo para instalá-lo:

    **No Windows:**
    - Baixe o FFmpeg para Windows a partir do site oficial do FFmpeg.
    - Após o download, extraia os arquivos e adicione o diretório bin ao PATH do seu sistema:
        - Copie o caminho da pasta bin onde o FFmpeg foi extraído.
        - Abra o menu "Iniciar" e pesquise por "variáveis de ambiente".
        - Clique em "Editar variáveis de ambiente do sistema" e depois em "Variáveis de ambiente".
        - Na seção "Variáveis do sistema", selecione a variável Path e clique em "Editar".
        - Adicione o caminho da pasta bin do FFmpeg à lista de variáveis e clique em "OK".

    **No Linux (Ubuntu/Debian):**
    - Abra o terminal e execute os seguintes comandos para instalar o FFmpeg:
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```
    **No macOS:**
    - No terminal, você pode usar o Homebrew para instalar o FFmpeg. Caso não tenha o Homebrew instalado, primeiro instale-o com o seguinte comando:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    - Depois, instale o FFmpeg com:
    ```bash
    brew install ffmpeg
    ```
5. **Executando o script**
    - Após instalar todas as dependências, o último passo é executar o script. Para isso, no terminal, dentro da pasta do projeto, execute o seguinte comando:
    ```bash
    python downloader.py
    ```

## Contribuindo
Se você quiser contribuir com melhorias para este projeto, fique à vontade para criar um **pull request**! Sinta-se livre para abrir **issues**, sugerir novas funcionalidades ou corrigir problemas existentes.