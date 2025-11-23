import os
import warnings
import glob
import time
import argparse
import whisper

# ==========================
# ⚙️ CONFIGURAÇÃO PADRÃO
# ==========================

# Valor padrão se o usuário NÃO passar --device
# Pode ser: "cpu", "cuda" ou "auto"
DEVICE_MODE_DEFAULT = "cpu"

# Pasta onde estão os áudios
# Exemplo Linux:  ~/Downloads/audios
# Exemplo Windows: C:\Users\SeuUsuario\Downloads\audios
DIR_AUDIOS = os.path.expanduser("~/Downloads/audios")

# Modelo do Whisper:
# menores = mais rápidos; maiores = melhor qualidade
# opções: "tiny", "base", "small", "medium"
MODEL_NAME = "small"

# Extensões de áudio suportadas pelo script
AUDIO_EXTENSIONS = [".ogg", ".mp3", ".wav", ".m4a", ".flac", ".webm", ".mp4"]


# ==========================
# 🧾 ARGPARSE (OPCIONAL)
# ==========================

parser = argparse.ArgumentParser(
    description="Transcrição em lote de arquivos de áudio usando Whisper."
)

parser.add_argument(
    "--device",
    choices=["cpu", "cuda", "auto"],
    help=(
        "Dispositivo de execução: "
        "'cpu' força CPU, "
        "'cuda' tenta usar GPU, "
        "'auto' tenta cuda e cai pra cpu se não tiver."
    ),
)

args = parser.parse_args()
DEVICE_MODE = args.device if args.device is not None else DEVICE_MODE_DEFAULT


# =========================================
# 🧠 SELEÇÃO DE DEVICE (CPU / CUDA / AUTO)
# =========================================

DEVICE = "cpu"  # default

if DEVICE_MODE == "cpu":
    # 🖥️ Modo CPU explícito:
    # - Esconde GPU só para ESTE processo
    # - Suprime warnings genéricos que só confundem
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    warnings.filterwarnings("ignore", category=UserWarning)
    print("🖥️  Modo selecionado: CPU (GPU será ignorada para este script).")

elif DEVICE_MODE in ("cuda", "auto"):
    import torch  # só importa se for realmente considerar CUDA

    if torch.cuda.is_available():
        DEVICE = "cuda"
        print("⚡  GPU detectada. Tentando usar CUDA...")
    else:
        DEVICE = "cpu"
        print("🖥️  CUDA não disponível, usando CPU.")
else:
    raise SystemExit(f"Valor inválido para DEVICE_MODE: {DEVICE_MODE}")


# ==========================
# 🚀 CARREGA MODELO WHISPER
# ==========================

print(f"Carregando modelo '{MODEL_NAME}' no dispositivo: {DEVICE} ...")
model = whisper.load_model(MODEL_NAME, device=DEVICE)


# ==========================
# 🎧 PROCURA ARQUIVOS DE ÁUDIO
# ==========================

files: list[str] = []

for ext in AUDIO_EXTENSIONS:
    pattern = os.path.join(DIR_AUDIOS, f"*{ext}")
    files.extend(glob.glob(pattern))

files = sorted(files)

print(
    f"Encontrei {len(files)} arquivos de áudio em {DIR_AUDIOS} "
    f"({', '.join(AUDIO_EXTENSIONS)})"
)
if not files:
    raise SystemExit(
        "Nenhum arquivo de áudio encontrado. "
        "Verifique o caminho da pasta e as extensões."
    )


# ==========================
# ⏱️ TIMER GLOBAL
# ==========================

start_global = time.time()


# ==========================
# 📝 LOOP DE TRANSCRIÇÃO
# ==========================

for idx, audio in enumerate(files, start=1):
    print(f"\n[{idx}/{len(files)}] Transcrevendo: {audio}")

    start_file = time.time()

    result = model.transcribe(
        audio,
        language="pt",              # força PT-BR
        fp16=(DEVICE == "cuda"),    # fp16 só faz sentido na GPU
    )

    elapsed_file = time.time() - start_file

    txt_path = audio + ".txt"
    with open(txt_path, "w", encoding="utf-8") as out:
        out.write(result["text"])

    print(f"   ✅ Transcrição salva em: {txt_path}")
    print(f"   ⏱️ Tempo deste arquivo: {elapsed_file:.1f} segundos")

elapsed_global = time.time() - start_global
print(f"\n🎉 Concluído! Tempo total de processamento: {elapsed_global:.1f} segundos.")
