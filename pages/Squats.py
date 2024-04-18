import streamlit as st
import winsound
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

frequency=2000
duration=800 #miliseconds
winsound.Beep(frequency,duration)

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

def error_calculate_angle(p,q,r):
    p = np.array(p) # First
    q = np.array(q) # Mid
    r = np.array(r) # End
    
    radians = np.arctan2(r[1]-q[1], r[0]-q[0]) - np.arctan2(p[1]-q[1], p[0]-q[0])
    error_angle = np.abs(radians*180.0/np.pi)
    
    if error_angle >180.0:
        error_angle = 360-error_angle
        
    return error_angle 






if st.button("Lets Go!!"):
    cap = cv2.VideoCapture(0)

# Curl counter variables
    squats_counter = 0 
    stage = None

## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
        
        # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
      
        # Make detection
            results = pose.process(image)
    
        # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark
            
            # Get coordinates
                leftHip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                leftKnee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                leftAnkle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                leftShoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            # Calculate angle
                angle = calculate_angle(leftHip, leftKnee, leftAnkle)
                error_angle = error_calculate_angle(leftKnee,leftHip, leftShoulder)
            # Visualize angle
                cv2.putText(image, str(angle), 
                               tuple(np.multiply(leftKnee, [640, 480]).astype(int)), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )
            #error_visualization
                cv2.putText(image, str(error_angle), 
                               tuple(np.multiply(leftHip, [640, 480]).astype(int)), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )
                if error_angle<120:
                    cv2.putText(image,'incorrect posture', 
                        (270,150), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2, cv2.LINE_AA),winsound.Beep(frequency,duration)
            
            # Curl counter logic
                if angle <140 :
                    stage = "down"
                if angle > 160 and stage =='down':
                    stage="up"
                    squats_counter +=1
                    print(squats_counter)
                       
            except:
                pass
        
        # Render curl counter
        # Setup status box
            cv2.rectangle(image, (0,0), (255,90), (245,117,16), -1)
        
        # Rep data
            cv2.putText(image, 'REPS', (15,12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, str(squats_counter), 
                        (10,60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        # Stage data
            cv2.putText(image, 'STAGE', (80,12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, stage, 
                        (90,60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
         #print exercise name
            cv2.putText(image,'Squats', 
                        (270,60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2, cv2.LINE_AA)
        
        
        # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )                   
        
            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    
        cap.release()
        cv2.destroyAllWindows()    
    