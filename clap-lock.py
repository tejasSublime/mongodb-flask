# import pyaudio
# import wave
# import time
# import os
# import struct
# import cv2
# import mediapipe as mp

# # Initialize the gesture recognizer

# # def clap_detection(stream):
# #     sound_level = 0.0
# #     for i in range(100):
# #         sample = stream.read(1, exception_on_overflow=False)
# #         if sample == b'':
# #             break
# #         sound_level += struct.unpack('f', sample)[0]
# #     # sound_level  = sound_level / 100
# #     time.sleep(1)
# #     print(sound_level )
# #     print(sound_level > 100)
# #     if sound_level > 100:
# #         return True
# #     else:
# #         return False

# BaseOptions = mp.tasks.BaseOptions
# GestureRecognizer = mp.tasks.vision.GestureRecognizer
# GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
# GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
# VisionRunningMode = mp.tasks.vision.RunningMode

# # Create a gesture recognizer instance with the live stream mode:
# def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
#     print('gesture recognition result: {}'.format(result))

# options = GestureRecognizerOptions(
#     base_options=BaseOptions("./gesture_recognizer.task"),
#     running_mode=VisionRunningMode.LIVE_STREAM,
#     result_callback=print_result)
# # with GestureRecognizer.create_from_options(options) as recognizer:
# mphands=mp.solutions.mediapipe.python.solutions.hands

# hannd=mphands.Hands()

# def openCamera(): 
#     # mp_gesture = mp.tasks.vision.GestureRecognizer()
#     # mp_gesture = mp.solutions.gesture.GestureRecognizer()
#     cap = cv2.VideoCapture(0)
#     # Start the video capture
#     results = []
#     with GestureRecognizer.create_from_options(options) as recognizer:
#         while True:
#         # Capture the current frame
#             ret, frame = cap.read()
             
#             img_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#             result= hannd.process(img_rgb)
#             # recognizer=GestureRecognizer.create_from_options(options)
#             # Process the frame with the gesture recognizer
#             # frame_timestamp_ms = int(cap.get(cv2.CAP_PROP_POS_MSEC))
#             # mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
#             # recognition_result =recognizer.recognize_async(mp_image,frame_timestamp_ms )
            
#             # print(recognition_result)
#             # hand_landmarks = recognition_result.hand_landmarks
#             # results.append((top_gesture, hand_landmarks))
#             # print_result(result=GestureRecognizerResult , output_image=mp_image , timestamp_ms=frame_timestamp_ms)
#             # d(images, results)
#             # print_result(output_image=mp_image , timestamp_ms=frame_timestamp_ms, result=GestureRecognizerResult)
#             # Check if a gesture was detected
#             if results.multi_handedness:
#                 for hand_landmarks in results.multi_hand_landmarks:
#                     # Get the gesture name
#                     gesture_name = results.classification[0].label

#                     # Print the gesture name
#                     print(f"Gesture detected: {gesture_name}")

#             # Display the frame
#             cv2.imshow("Frame", frame)

#             # Check if the user wants to quit
#             key = cv2.waitKey(1)
#             if key == 27:
#                 break

#     cap.release()
#     cv2.destroyAllWindows()                     
# def lock_computer():
   
#     os.system("rundll32.exe user32.dll,LockWorkStation")

# if __name__ == "__main__":
#     # stream = pyaudio.PyAudio().open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True, frames_per_buffer=1024)
#     openCamera()
#     # while True:
       
#     #     # if clap_detection(stream):
#     #     #     print("Clap detected! Locking computer...")
#     #     #     lock_computer()
#     #     #     break
#     #     if :
#     #         print("Clap detected! Locking computer...")
#     #         lock_computer()
#     #         break

#     time.sleep(0.1)