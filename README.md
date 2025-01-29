Here's a `README.md` for your audio visualizer project:

```markdown
# Audio Visualizer in Python

This is a simple Python-based audio visualizer that records audio and generates two plots:
1. **Waveform**: The graphical representation of the audio signal in the time domain.
2. **Frequency Spectrum**: The Fourier transform of the audio data showing the frequencies present in the signal.

## Requirements

To run this project, you need the following Python libraries:

- `numpy`
- `matplotlib`
- `sounddevice`
- `scipy`

You can install them using the following command:

```bash
pip install numpy matplotlib sounddevice scipy
```

## How to Use

1. Clone or download this repository to your local machine.
2. Run the script `audio_visualizer.py` in your Python environment.
3. The script will record audio for 5 seconds and generate two plots:
   - **Waveform**: A plot showing how the audio signal varies over time.
   - **Frequency Spectrum**: A plot showing the frequency content of the audio signal.

## Code Overview

### 1. **Audio Recording**:
The script uses the `sounddevice` library to record audio for a given duration and sampling rate.

### 2. **Waveform Plot**:
The time-domain audio waveform is generated using `matplotlib`. The x-axis represents time, and the y-axis represents the audio signal's amplitude.

### 3. **Frequency Spectrum Plot**:
The Fourier Transform (FFT) is computed using `scipy.fft` to convert the audio data from the time domain to the frequency domain. The positive frequencies are plotted on the x-axis, and the amplitude of the frequencies is plotted on the y-axis.

## Running the Code

Run the following command to start the script:

```bash
python audio_visualizer.py
```

## Credits

Made by Shashank Singh.
