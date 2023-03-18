# EEGfeedback
Python code associated to the paper on evaluating EEG-based BCIs in education
Python code for collecting data recorded by a Muse BCI (https://choosemuse.com/) and providing real-time feedback to participants to a guitar training session.

It uses the muselsl library (https://pypi.org/project/muselsl/) to connect to a Muse device, collect data from the device, and calculate power in the alpha and beta frequency bands. It then uses the pyautogui library (https://pypi.org/project/PyAutoGUI/) to provide real-time feedback to the participant to the experiment, based on their alpha power level. The feedback is provided as an alert message on the screen of the laptop.

Note that the code only collects data and provides feedback for a fixed duration of 30 seconds, as defined by the duration variable. This can be modified to suit the needs of the experiment.
