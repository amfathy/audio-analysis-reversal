import os
import numpy as np
import scipy.io.wavfile as wave
import wave as wave_module

#defult 16 bit per sample
#check lwa7do hal 8 wla 16
def get_bits_per_sample(filepath):
    with wave_module.open(filepath, 'rb') as wf:
        return wf.getsampwidth() * 8
#retuen kam bit kul sample

def calculate_data_characteristics(filepath):
    samplerate, data = wave.read(filepath)
#read data
#samplerate (tdafok data)
    length = len(data) / samplerate
    data_size_samples = len(data)
#kwanin used
    #need to know data 3andha kam bit
    data_size_bits = data_size_samples * get_bits_per_sample(filepath)

    #mo3dl tdafok bits in seconds
    bit_rate = samplerate * get_bits_per_sample(filepath)
    
    type_of_recording = "mono" if len(data.shape) == 1 else "stereo"

    sampling_rate = samplerate

    return {
        "Length": length,

        "Sampling Rate": sampling_rate,

        "Data Size (Samples)": data_size_samples,

        "Data Size (Bits)": data_size_bits,

        "Bit Rate": bit_rate,

        "Type of Recording": type_of_recording,
    }
#return kam sample f sania
def reverse_and_save_audio(filepath):
    samplerate, data = wave.read(filepath)

    reversed_data = np.flipud(data)
    reversed_file_path = os.path.splitext(filepath)[0] + "_reversed.wav"

    wave.write(reversed_file_path, samplerate, reversed_data)

    print(f"Reversed audio saved to: {reversed_file_path}")

file_path = 'three.wav'
if os.path.exists(file_path):
    bits_per_sample = get_bits_per_sample(file_path)
    print(f"Bits per sample: {bits_per_sample}")

    characteristics = calculate_data_characteristics(file_path)
    for key, value in characteristics.items():

        print(f"{key}: {value}")

    reverse_and_save_audio(file_path)
else:
    print("File not found.")
