# 🎧➡️📝 Transcrição Automática de Áudios para Texto

Este repositório contém um script simples e eficiente para **transcrever automaticamente áudios do WhatsApp e outras gravações** para arquivos `.txt`, utilizando o modelo **Whisper**, de forma totalmente **local** e **sem depender de APIs pagas**.

Suporta diversos formatos:

* `.ogg`
* `.mp3`
* `.wav`
* `.m4a`
* `.flac`
* `.webm`
* `.mp4` (quando contém áudio)

---

## 💡 Motivação

Você possui um grande volume de áudios do WhatsApp ou outros áudios gravados? 📱🎧
E precisa transformar isso em texto para:

* Revisar conversas longas 📚
* Fazer buscas rápidas 🔍
* Guardar registros importantes 📝
* Montar relatórios ou resumos 📄

Fazer isso **manualmente** é inviável.

👉 Com este script, basta colocar **todos os áudios em uma pasta** e rodar o script.
Ele gera um **.txt** para cada arquivo automaticamente.

Tudo isso **localmente**, sem custo e preservando sua privacidade.

---

## 🚀 Funcionalidade Principal

O script:

* Procura arquivos de áudio com estas extensões:

  ```
  .ogg, .mp3, .wav, .m4a, .flac, .webm, .mp4
  ```

* Transcreve cada arquivo usando o modelo Whisper

* Gera um arquivo `.txt` com o mesmo nome

* Mostra:

  * ⏱️ Tempo por arquivo
  * ⏱️ Tempo total da pasta

* Permite escolher o modo de execução:

  * 🖥️ **CPU**
  * ⚡🟩 **CUDA (GPU NVIDIA)**
  * 🎛️ **AUTO** (tenta GPU → se falhar, usa CPU)

---

# 🧠 Modos de Execução (Device Modes)

| Modo   | Ícone | Descrição                                                                          |
| ------ | ----- | ---------------------------------------------------------------------------------- |
| `cpu`  | 🖥️   | Força execução no processador. Mais lento, porém compatível com todas as máquinas. |
| `cuda` | ⚡🟩   | Força execução na GPU NVIDIA compatível. Muito mais rápido.                        |
| `auto` | 🎛️   | Tenta usar GPU → se não existir ou não for compatível, cai para CPU.               |

### 🟢 Por que preferir CUDA sempre que possível?

Quando suportado:

* 🔥 Transcrição muito mais rápida
* 📦 Permite modelos maiores
* 🎧 Ideal para grandes lotes de áudios
* 🧵 Libera a CPU para outras tarefas

> ⚠️ Observação: GPUs mais antigas (ex.: algumas MX) podem não ser suportadas pelo PyTorch moderno.
> Nesses casos, utilize o modo `cpu`.

---

# 🏗️ Estrutura esperada

```
audio-transcription/
 ├── main.py
 ├── requirements.txt
 └── (pasta dos áudios)
```

### Exemplos de pasta de áudios:

* **Linux:** `~/Downloads/audios/`
* **Windows:** `C:\Users\SeuUsuario\Downloads\audios\`

Basta colocar todos os arquivos suportados nessa pasta.

---

# ▶️ Como usar

## 1️⃣ Modo básico (usa o device padrão configurado no script)

```bash
python3 main.py
```

---

## 2️⃣ Selecionando o modo de execução

### 🖥️ Forçar CPU:

```bash
python3 main.py --device cpu
```

### ⚡ Forçar CUDA (se suportado):

```bash
python3 main.py --device cuda
```

### 🎛️ Automático:

```bash
python3 main.py --device auto
```

---

# 🔧 Pré-requisitos

* Python 3.9+
* ffmpeg instalado (obrigatório)
* Whisper + Torch
* Ambiente virtual (`venv`) recomendado

---

# 🎬 Instalação do FFmpeg

## 🐧 Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg
```

Verificar:

```bash
ffmpeg -version
```

---

## 🪟 Windows — instalar e adicionar ao PATH

1. Baixe o FFmpeg:
   [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Baixe o pacote “release full-build” (ZIP)
3. Extraia em:

```
C:\ffmpeg\
```

4. Adicione ao PATH via CMD como Administrador:

```cmd
setx /M PATH "%PATH%;C:\ffmpeg\bin"
```

5. Teste:

```cmd
ffmpeg -version
```

---

# 🧪 Ambiente Virtual (venv)

## 🐧 Linux – criar e ativar

Criar:

```bash
python3 -m venv .venv
```

Ativar:

```bash
source .venv/bin/activate
```

Desativar:

```bash
deactivate
```

---

## 🪟 Windows – criar e ativar

Criar:

```powershell
python -m venv .venv
```

Ativar:

```powershell
.\.venv\Scripts\activate
```

Desativar:

```powershell
deactivate
```

---

# 📦 Instalando dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

---

# 📚 Bibliotecas utilizadas

| Biblioteca | Função                             |
| ---------- | ---------------------------------- |
| `whisper`  | Transcrição local                  |
| `torch`    | Backend de execução (CPU/GPU)      |
| `argparse` | Opção `--device` via CLI           |
| `glob`     | Busca de arquivos                  |
| `time`     | Cronometragem                      |
| `warnings` | Suprime avisos indesejados         |
| `os`       | Manipulação de diretórios/ambiente |

---

# 📁 requirements.txt recomendado

```text
openai-whisper
torch
```

Versão apenas CPU:

```text
openai-whisper
# pip install torch --index-url https://download.pytorch.org/whl/cpu
```

---

# 🎉 Tudo pronto para transcrever!

📍 Coloque seus áudios em:

* **Linux:** `~/Downloads/audios/`
* **Windows:** `C:\Users\SeuUsuario\Downloads\audios\`

📍 Ative seu ambiente virtual
📍 Rode:

```bash
python3 main.py
```

Relaxe, tome um café ☕
e deixe o script transformar seus áudios em texto automaticamente ✨📜

---

# 📜 Licença

Este projeto é licenciado sob a MIT License — uma licença permissiva e amplamente adotada pela comunidade open-source.

Isso significa que você pode:

* Usar
* Modificar
* Distribuir
* Incorporar em projetos pessoais ou comerciais

…desde que mantenha o aviso de copyright e a licença original nos arquivos redistribuídos.