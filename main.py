from utils import read_video, save_video
from trackers import Tracker

def main():
    # Read video
    video_frames = read_video('/teamspace/studios/this_studio/input_video/08fd33_4.mp4')

    # Initialize Tracker
    tracker = Tracker('/teamspace/studios/this_studio/models/best.pt')
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='/teamspace/studios/this_studio/stubs/track_stubs.pkl')

    # Draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Save video
    save_video(output_video_frames, '/teamspace/studios/this_studio/output_videos/output_video.avi')

if __name__ == '__main__':
    main()