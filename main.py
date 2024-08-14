from utils import read_video, save_video

def main():
    # Read video
    video_frames = read_video('/teamspace/studios/this_studio/input_video/08fd33_4.mp4')

    # Save video
    save_video(video_frames, '/teamspace/studios/this_studio/output_videos/output_video.avi')

if __name__ == '__main__':
    main()