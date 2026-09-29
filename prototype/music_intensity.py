
import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sys
import os

# === SETTINGS ===
FRAME_SIZE = 2048
HOP_LENGTH = 512

def compute_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)

    # RMS energy
    rms = librosa.feature.rms(y=y, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]

    # Spectral flux
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=HOP_LENGTH)

    # Chroma entropy (proxy for harmonic complexity)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr, hop_length=HOP_LENGTH)
    chroma_entropy = -np.sum(chroma * np.log2(chroma + 1e-6), axis=0) / np.log2(chroma.shape[0])

    # Normalize features to 0–1
    def normalize(x): return (x - np.min(x)) / (np.max(x) - np.min(x) + 1e-6)
    rms_norm = normalize(rms)
    flux_norm = normalize(onset_env)
    entropy_norm = normalize(chroma_entropy)

    # Combine into a single intensity curve
    intensity = 0.5 * rms_norm + 0.3 * flux_norm + 0.2 * entropy_norm

    times = librosa.times_like(rms, sr=sr, hop_length=HOP_LENGTH)
    return times, rms_norm, flux_norm, entropy_norm, intensity

def plot_features(times, rms, flux, entropy, intensity, title):
    plt.figure(figsize=(12, 6))
    plt.plot(times, rms, label="RMS Energy", alpha=0.7)
    plt.plot(times, flux, label="Spectral Flux", alpha=0.7)
    plt.plot(times, entropy, label="Harmonic Entropy", alpha=0.7)
    plt.plot(times, intensity, label="Combined Intensity", color="black", linewidth=2)
    plt.title(f"Musical Intensity Analysis – {title}")
    plt.xlabel("Time (s)")
    plt.ylabel("Normalized Value")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python music_intensity.py <audiofile.wav>")
        sys.exit(1)

    audio_path = sys.argv[1]
    if not os.path.exists(audio_path):
        print(f"File not found: {audio_path}")
        sys.exit(1)

    times, rms, flux, entropy, intensity = compute_features(audio_path)
    plot_features(times, rms, flux, entropy, intensity, os.path.basename(audio_path))
