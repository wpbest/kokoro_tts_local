import os
import platform
import torch
from kokoro import KPipeline
import soundfile as sf  # For saving WAV files

def main():
    print("🔊 Initializing Kokoro TTS Local (Official API)")

    # Device selection (GPU preferred)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    device_name = torch.cuda.get_device_name(0) if device == "cuda" else "CPU only"
    print(f"🧠 Using device: {device.upper()} ({device_name})")

    # Initialize Kokoro speech pipeline
    try:
        pipeline = KPipeline(lang_code="a")  # American English
        print("✅ Pipeline initialized (auto-download/cached if needed).")
    except Exception as e:
        print(f"❌ Error initializing pipeline: {e}")
        print("💡 Check that dependencies (e.g., eSpeak-NG) are installed, then try again.")
        return

    print("Type text to synthesize (or 'quit' to exit).")

    while True:
        text = input("\nEnter text: ").strip()
        if text.lower() == "quit":
            print("👋 Goodbye.")
            break
        if not text:
            continue

        print("🎙️ Generating speech...")
        try:
            generator = pipeline(text, voice="af_heart")

            audio_chunks = []
            for gs, ps, audio in generator:
                # Ensure numeric formatting even if values are strings
                try:
                    gs_val = float(gs)
                    ps_val = float(ps)
                    print(f"  Chunk: Gen speed {gs_val:.2f}x | Pron speed {ps_val:.2f}x")
                except Exception:
                    print(f"  Chunk: Gen speed {gs} | Pron speed {ps}")

                audio_chunks.append(audio)

            if audio_chunks:
                full_audio = torch.cat(audio_chunks)
                filename = "output.wav"
                sf.write(filename, full_audio, 24000)  # 24kHz
                print(f"✅ Audio saved to {filename}")

                # Cross-platform playback
                if os.name == "nt":
                    os.system(f'start {filename}')
                elif platform.system() == "Darwin":
                    os.system(f'open {filename}')
                else:
                    os.system(f'xdg-open {filename}')
            else:
                print("⚠️ No audio generated (empty or invalid text).")

        except Exception as e:
            print(f"❌ Error generating audio: {e}")

if __name__ == "__main__":
    main()
