# Football Analytics Pipeline

This project is a football analytics pipeline that takes a video of a football match as input and outputs a video with various analytics features, including player tracking, team assignment, ball possession, speed and distance estimation, and camera movement estimation.

## Features

- **Player Tracking**: Tracks the movement of each player on the field.
- **Team Assignment**: Assigns players to their respective teams based on jersey color.
- **Ball Possession**: Determines which player is in possession of the ball.
- **Speed and Distance Estimation**: Calculates the speed and distance covered by each player.
- **Camera Movement Estimation**: Estimates the movement of the camera during the match.
- **View Transformation**: Transforms the perspective of the video to a top-down view.

## Requirements

- Python 3.7+
- OpenCV
- Ultralytics YOLO
- NumPy

## Installation

1. **Clone the repository:**
    ```bash
    git https://github.com/ROBERT-ADDO-ASANTE-DARKO/Football-Analysis-with-YOLOv8-and-OpenCV.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd Football-Analysis-with-YOLOv5-and-OpenCV
    ```
3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Place the video file you want to analyze in the `input_video` directory.**
2. **Run the main script:**
    ```bash
    python main.py
    ```
3. **The output video will be saved in the `output_videos` directory.**

## File Structure

```plaintext
Football-Analysis-with-YOLOv5-and-OpenCV/
├── main.py                      # Main script
├── utils.py                     # Utility functions
├── trackers.py                  # Object tracking module
├── team_assigner.py             # Team assignment module
├── player_ball_assigner.py       # Ball possession assignment module
├── camera_movement_estimator.py  # Camera movement estimation module
├── view_transformer.py           # View transformation module
├── speed_and_distance_estimator.py # Speed and distance estimation module
├── input_video/                 # Input video files
├── output_videos/               # Output video files
├── models/                      # Trained YOLO model
└── stubs/                       # Stub files for intermediate results
