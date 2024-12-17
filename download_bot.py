import os
import json
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from threading import Thread
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Definir credenciais do Spotify (Substitua pelos seus valores)
CLIENT_ID = "9349e103383d4c86b66baa4a4052f2d9"
CLIENT_SECRET = "78daae44f01e40248051155997306180"

# Autenticação no Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Função para salvar a pasta destino no arquivo config.json
def save_config(destination_folder):
    with open('config.json', 'w') as config_file:
        json.dump({'destination_folder': destination_folder}, config_file)

# Função para carregar a pasta destino do arquivo config.json
def load_config():
    if os.path.exists('config.json'):
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            return config.get('destination_folder', '')
    return ''

# Função para atualizar a barra de progresso
def update_progress(percent, progress_var, progress_bar):
    progress_var.set(percent)
    progress_bar.update()

# Função de download do áudio
def download_audio(url, destination_folder, progress_var, progress_bar, status_label):
    # Tentar baixar do YouTube usando yt-dlp
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(destination_folder, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',  # Definir o formato de saída como MP4
            'progress_hooks': [lambda d: progress_hook(d, progress_var, progress_bar, status_label)]
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Download completo", "O vídeo foi baixado com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função de hook para a barra de progresso
def progress_hook(d, progress_var, progress_bar, status_label):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
        downloaded_bytes = d.get('downloaded_bytes', 0)
        percent = int(downloaded_bytes / total_bytes * 100) if total_bytes > 0 else 0
        speed = d.get('speed', 0) or 0
        size_in_mib = total_bytes / 1024 / 1024 if total_bytes > 0 else 0
        speed_in_kib = speed / 1024 if speed > 0 else 0
        update_progress(percent, progress_var, progress_bar)
        status_label.config(text=f"Baixando: {percent}% - Velocidade: {speed_in_kib:.2f} KiB/s - Tamanho: {size_in_mib:.2f} MiB")
    elif d['status'] == 'finished':
        update_progress(100, progress_var, progress_bar)
        status_label.config(text="Download concluído")

# Função para buscar faixas no Spotify
def get_spotify_tracks(url):
    tracks = []
    try:
        if "spotify.com" in url:
            # Extrair ID da playlist
            playlist_id = url.split("/")[-1].split("?")[0]
            results = sp.playlist_tracks(playlist_id)
            for item in results['items']:
                track = item['track']
                track_name = track['name']
                artist_name = track['artists'][0]['name']
                tracks.append(f"{track_name} {artist_name}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao obter as faixas do Spotify: {str(e)}")
    return tracks

# Função para iniciar o download em uma thread separada
def start_download():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira o link do vídeo ou playlist do Spotify.")
        return

    destination_folder = destination_folder_var.get()
    if not destination_folder:
        messagebox.showwarning("Aviso", "Por favor, escolha a pasta de destino.")
        return

    save_config(destination_folder)

    download_thread = Thread(target=download_from_url, args=(url, destination_folder, progress_var, progress_bar, status_label))
    download_thread.start()

# Função para baixar música do YouTube ou Spotify
def download_from_url(url, destination_folder, progress_var, progress_bar, status_label):
    if "spotify.com" in url:
        tracks = get_spotify_tracks(url)
        if not tracks:
            messagebox.showwarning("Aviso", "Nenhuma faixa encontrada na playlist do Spotify.")
            return
        for track in tracks:
            search_url = f"https://www.youtube.com/results?search_query={track}"
            download_audio(search_url, destination_folder, progress_var, progress_bar, status_label)
    else:
        download_audio(url, destination_folder, progress_var, progress_bar, status_label)

# Função para selecionar a pasta de destino
def select_destination_folder():
    folder = filedialog.askdirectory()
    if folder:
        destination_folder_var.set(folder)

# GUI
root = tk.Tk()
root.title("YouTube e Spotify Video Downloader")
root.geometry("500x350")

# Centralizar os widgets no root
frame = tk.Frame(root)
frame.pack(expand=True)

# URL Entry
tk.Label(frame, text="Link do Vídeo ou Playlist do Spotify:").pack(pady=5)
url_entry = tk.Entry(frame, width=60)
url_entry.pack(pady=5)

# Destination Folder
tk.Label(frame, text="Pasta de Destino:").pack(pady=5)
destination_folder_var = tk.StringVar()
destination_folder_var.set(load_config())

destination_frame = tk.Frame(frame)
destination_frame.pack(pady=5)
tk.Entry(destination_frame, textvariable=destination_folder_var, width=50).pack(side=tk.LEFT, padx=5)
tk.Button(destination_frame, text="Selecionar", command=select_destination_folder).pack(side=tk.LEFT, padx=5)

# Progress Bar
tk.Label(frame, text="Progresso:").pack(pady=5)
progress_var = tk.IntVar()
progress_bar = Progressbar(frame, orient=tk.HORIZONTAL, length=400, mode='determinate', maximum=100, variable=progress_var)
progress_bar.pack(pady=5)

# Status Label
status_label = tk.Label(frame, text="Aguardando...")
status_label.pack(pady=5)

# Download Button
tk.Button(frame, text="Baixar Vídeo", command=start_download).pack(pady=20)

root.mainloop()
