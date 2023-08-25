import os
import cv2
import datetime
import numpy as np
import time
from win32api import GetSystemMetrics
from PIL import ImageGrab

def record_screen():
    """
    Record the screen and save it as an MP4 file in the current directory.
    """

    # Get the current directory where the code is located.
    current_directory = os.getcwd()

    # Get the width and height of the screen.
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    # Create a timestamp for the filename.
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Create a filename for the MP4 file.
    file_name = os.path.join(current_directory, f'{time_stamp}.mp4')

    # Create a VideoWriter object.
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

    # Start recording.
    while True:
        # Get a screenshot of the screen.
        img = ImageGrab.grab(bbox=(0, 0, width, height))

        # Convert the screenshot to a NumPy array.
        img_np = np.array(img)

        # Convert the NumPy array to an RGB image.
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        # Display the image on the screen.
        cv2.imshow('Screen Recorder', img_final)

        # Write the image to the MP4 file.
        captured_video.write(img_final)

        # Check if the user wants to stop recording.
        if cv2.waitKey(10) == ord('q'):
            break

    # Stop recording and close the VideoWriter object.
    captured_video.release()

    # Close all OpenCV windows.
    cv2.destroyAllWindows()

if __name__ == '__main__':
    record_screen()
