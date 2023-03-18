# Import necessary libraries
from muselsl import stream, list_muses
import numpy as np
import time
import pyautogui

# Define variables
sampling_rate = 256
duration = 30 # in seconds
feedback_threshold = 0.5

# Find available Muse devices
muselist = list_muses()

# Connect to first available Muse device
if not muselist:
    print('No Muses found')
else:
    muse = muselist[0]
    stream_name = muse['name']
    stream_address = muse['address']
    print('Connecting to ' + stream_name + ' at ' + stream_address)
    stream_inlet = stream(stream_name, stream_address)

    # Start data collection and feedback loop
    start_time = time.time()
    feedback_time = start_time + duration
    while time.time() < feedback_time:
        # Collect data from the Muse device
        sample, timestamp = stream_inlet.pull_sample()
        eeg_data = np.array(sample[:4])

        # Calculate power in alpha and beta bands
        alpha_power = np.mean(eeg_data[8:13])
        beta_power = np.mean(eeg_data[13:30])

        # Check if alpha power is greater than threshold and provide feedback
        if alpha_power > feedback_threshold:
            pyautogui.alert('Keep going!')
        else:
            pyautogui.alert('Try to focus more!')

        # Delay to match sampling rate
        time.sleep(1/sampling_rate)

    # Disconnect from Muse device
    stream_inlet.close()
