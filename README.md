# Football Analytics Pipeline
This project is a football analytics pipeline that takes a video of a football match as input and outputs a video with player tracking, team assignment, ball possession, speed and distance estimation, and camera movement estimation.

Features
Player Tracking: Tracks the movement of each player on the field.
Team Assignment: Assigns players to their respective teams based on jersey color.
Ball Possession: Determines which player is in possession of the ball.
Speed and Distance Estimation: Calculates the speed and distance covered by each player.
Camera Movement Estimation: Estimates the movement of the camera during the match.
View Transformation: Transforms the perspective of the video to a top-down view.
Requirements
Python 3.7+
OpenCV
Ultralytics YOLO
NumPy
Installation
Clone the repository:
git clone https://github.com/your-username/football-analytics-pipeline.git
Install the required packages:
pip install -r requirements.txt
Usage
Place the video file you want to analyze in the input_video directory.
Run the main script:
python main.py
The output video will be saved in the output_videos directory.
File Structure
football-analytics-pipeline/
├── main.py                    # Main script
├── utils.py                   # Utility functions
├── trackers.py                # Object tracking module
├── team_assigner.py           # Team assignment module
├── player_ball_assigner.py    # Ball possession assignment module
├── camera_movement_estimator.py # Camera movement estimation module
├── view_transformer.py        # View transformation module
├── speed_and_distance_estimator.py # Speed and distance estimation module
├── input_video/               # Input video files
├── output_videos/              # Output video files
├── models/                    # Trained YOLO model
└── stubs/                     # Stub files for intermediate results
Notes
The accuracy of the pipeline depends on the quality of the input video and the trained YOLO model.
The pipeline is currently configured to work with videos of a specific resolution and frame rate. You may need to adjust the code if your input video has different specifications.
Future Work
Improve the accuracy of the pipeline by using more advanced tracking and estimation algorithms.
Add support for more features, such as player identification and event detection.
Create a user interface for easier interaction with the pipeline.