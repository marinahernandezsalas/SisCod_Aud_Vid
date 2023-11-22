import subprocess
import os

##EX1
class macroblocks:
    def generate_macroblocks_video(output_path, video_path):
        # Run FFMpeg command to generate video with macroblocks and motion vectors
        base_name, ext = os.path.splitext(os.path.basename(video_path))
        command = f"ffmpeg -hide_banner -flags2 +export_mvs -i {video_path} -vf codecview=mv=pf+bf+bb -an {output_path}"
        subprocess.run(command, shell=True, check=True)
    def __init__(self, video_path):
        self.video_path = video_path
    def create_new_bbb_container(self, output_path):
        start_time = 0
        duration = 50
        #Cut the BBB video into 50 seconds only
        cut_video_path = 'EX2_bbb_cut_50s.mp4'
        subprocess.run(['ffmpeg', '-i', self.video_path, '-ss', str(start_time), '-t', str(duration), cut_video_path])
        #Export BBB(50s) audio as MP3 mono track
        mono_audio_path = 'bbb_mono_audio.mp3'
        subprocess.run(['ffmpeg', '-i', cut_video_path, '-vn', '-ac', '1', mono_audio_path])
        #Export BBB(50s) audio in MP3 stereo with lower bitrate
        stereo_audio_path = 'bbb_stereo_audio.mp3'
        subprocess.run(['ffmpeg', '-i', cut_video_path, '-vn', '-ac', '2', '-b:a', '64k', stereo_audio_path])
        #Export BBB(50s) audio in AAC codec
        aac_audio_path = 'bbb_aac_audio.aac'
        subprocess.run(['ffmpeg', '-i', cut_video_path, '-vn', '-c:a', 'aac', aac_audio_path])
        #Package everything in a .mp4 container with FFMpeg
        subprocess.run(['ffmpeg', '-i', cut_video_path, '-i', mono_audio_path, '-i', stereo_audio_path, '-i', aac_audio_path, '-c:v', 'copy', '-c:a', 'copy', output_path])
        #Clean up the temporary files
        subprocess.run(['rm', cut_video_path, mono_audio_path, stereo_audio_path, aac_audio_path])
    def count_tracks(self):
        probe_command = ['ffprobe', '-v', 'error', '-select_streams', 'a:0', '-show_entries', 'stream=index', '-of', 'csv=p=0', self.video_path]
        output = subprocess.check_output(probe_command, universal_newlines=True)
        track_count = len(output.strip().split('\n'))
        return track_count

##EXAMPLE EX1
video_path = 'Big_Buck_Bunny.mp4'
output_path = 'EX1_macroblocks_BBB.mp4'
#Generate the video with macroblocks and motion vectors and save it
macroblocks.generate_macroblocks_video(output_path, video_path)

##EXAMPLE EX2
video_processor_ex2 = macroblocks('bbb.mp4')
#Create the new BBB container and save it
video_processor_ex2.create_new_bbb_container('EX2_new_bbb_container.mp4')

##EXAMPLE EX3
video_processor_ex3 = macroblocks('EX2_new_bbb_container.mp4')
#Get the number of tracks in the MP4 container
track_count = video_processor_ex3.count_tracks()
print(f"The MP4 container contains {track_count} tracks.")

##EX 5
import sys
sys.path.append('/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid')  # Add the path to the directory containing rgb_yuv.py

from EX4_Semi2 import subtitles
video_processor = subtitles('/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/Big_Buck_Bunny.mp4', '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/Toy Story (1995).srt')
#Integrate the subtitles into the video and save it
video_processor.integrate_subtitles('EX_4_video_with_subtitles.mp4')