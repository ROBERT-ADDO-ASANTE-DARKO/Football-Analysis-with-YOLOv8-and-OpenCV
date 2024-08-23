from utils import read_video, save_video
from trackers import Tracker
import cv2
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner

def main():
    # Read video
    video_frames = read_video('/teamspace/studios/this_studio/input_video/08fd33_4.mp4')

    # Initialize Tracker
    tracker = Tracker('/teamspace/studios/this_studio/models/best.pt')
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='/teamspace/studios/this_studio/stubs/track_stubs.pkl')

    # Interpolate ball positions
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])

    # Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], tracks['players'][0])

    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num], track['bbox'], player_id)
            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    # Assign ball acquisition
    player_assigner = PlayerBallAssigner()
    team_ball_control = []
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
        else:
            team_ball_control.append(team_ball_control[-1])

    # Save cropped image of a player
    '''
    for track_id, player in tracks['players'][0].items():
        bbox = player['bbox']
        frame = video_frames[0]

        # Crop bbox from frame
        cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

        # Save the cropped image
        cv2.imwrite(f'/teamspace/studios/this_studio/output_videos/crooped_image.jpg', cropped_image)
        break
    '''

    # Draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control)

    # Save video
    save_video(output_video_frames, '/teamspace/studios/this_studio/output_videos/output_video.avi')

if __name__ == '__main__':
    main()