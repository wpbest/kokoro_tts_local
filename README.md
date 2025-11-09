# kokoro_tts_local
kokoro_tts_local A Super-fast, offline Python text-to-speech app using Kokoro-TTS — no API keys, no cloud, just local voice generation.

# Hugging Space
pip install -U huggingface_hub

# Download the libraries
python -c "from huggingface_hub import snapshot_download; snapshot_download('hexgrad/Kokoro-82M', local_dir='./kokoro-models', local_dir_use_symlinks=False)"

⚙️ Step 1 — GPU setup commands (CUDA 12.1 for RTX 4070)

Run these before installing requirements:

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 --no-cache-dir

This ensures you get the CUDA 12.1 PyTorch build that perfectly matches your GPU.

pip install -r requirements.txt

# 🎧 Kokoro TTS Local  
Ultra-fast, **GPU-accelerated offline text-to-speech (TTS)** using the official **Kokoro** model (Hexgrad) and PyTorch.  
This app runs entirely **locally** after first-time model caching — no API keys, no cloud calls.

---

## 🚀 Features
- 🧠 **Uses your GPU** (RTX 4070 / CUDA 12.1 or higher)
- 🔊 **Offline voice generation** once model cached
- ⚙️ **KPipeline API** – official Kokoro TTS interface
- 💾 **Auto-save & playback** of generated `.wav` files
- 🧩 **Cross-platform** (Windows / Linux / macOS)
- ⚡ **Fast, lightweight, single-file app**

---

## 🧰 Prerequisites
- **Python 3.11 or newer**
- **NVIDIA GPU + CUDA 12.1 drivers**
- (Optional) **Developer Mode on Windows** for Hugging Face symlinks  
  👉 [Enable Developer Mode](https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development)

---

## 🧱 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-user>/kokoro_tts_local.git
   cd kokoro_tts_local

Create & activate a venv (recommended)

python -m venv .venv
.\.venv\Scripts\activate      # Windows
# source .venv/bin/activate   # Linux/macOS


Install GPU-optimized PyTorch (for RTX 4070 / CUDA 12.1)

pip uninstall torch torchvision torchaudio -y
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 --no-cache-dir


Install Kokoro and other dependencies

pip install -r requirements.txt

🗣️ Usage

Run the program:

python kokoro_tts_local.py


Example:

Enter text: Hello William! Kokoro TTS Local is running on GPU.
🎙️ Generating speech...
  Chunk: Gen speed 5.23x | Pron speed 0.97x
✅ Audio saved to output.wav


Output file: output.wav (24 kHz, playable instantly).

⚡ First-Run Notes

The Kokoro model (hexgrad/Kokoro-82M) downloads automatically the first time.

Files are cached under ~/.cache/huggingface/hub/ for offline use.

To clear or reset the cache:

Remove-Item -Recurse -Force "$env:USERPROFILE\.cache\huggingface\hub\models--hexgrad--Kokoro-82M"

🧩 Optional Enhancements

Install faster model downloader:

pip install huggingface_hub[hf_xet]


Change voices:

generator = pipeline(text, voice="af_heart")  # try other voices like 'am_moon', 'bf_dream', etc.


Switch accent:

pipeline = KPipeline(lang_code="b")  # British English

💡 Troubleshooting
Issue	Fix
IncompleteRead during download	Clear cache and re-run app
symlink warning on Windows	Enable Developer Mode
Unknown format code 'f'	Fixed in latest version (casts non-float values)
Slow or CPU-only	Ensure correct CUDA build of PyTorch installed
Speech too fast/slow	Adjust voice model or sampling rate

Includes open-source model files from hexgrad/Kokoro-82M
.


---

## 📦 **requirements.txt**

```txt
# --- Core dependencies ---
kokoro
soundfile
numpy
scipy

# --- GPU-accelerated PyTorch stack (install from index-url separately) ---
# torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# --- Optional performance improvement ---
huggingface_hub[hf_xet]


✅ Summary

After you publish this:

Anyone can clone your repo.

Run the CUDA-ready pip commands.

Get the same working Kokoro TTS Local you have — fully GPU-accelerated and offline.

Would you like me to append a short “Voices Table” (listing all Kokoro voices with example names like af_heart, am_moon, etc.) to the README? It makes your repo look even more polished.