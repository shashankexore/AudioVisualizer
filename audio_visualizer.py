import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fft import fft

# Set parameters
duration = 5  # Duration in seconds
sampling_rate = 44100  # Sampling rate (Hz)

# Record audio
print("Recording audio...")
audio_data = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=1, dtype='float32')
sd.wait()

# Create time axis for the waveform
time = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)

# Plot the audio waveform
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, audio_data)
plt.title('Audio Waveform')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Compute the Fourier Transform of the audio data
frequencies = np.fft.fftfreq(len(audio_data), 1 / sampling_rate)
spectrum = np.abs(fft(audio_data.flatten()))

# Plot the frequency spectrum
plt.subplot(2, 1, 2)
plt.plot(frequencies[:len(frequencies)//2], spectrum[:len(frequencies)//2])  # Plot positive frequencies
plt.title('Frequency Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
