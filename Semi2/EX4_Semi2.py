import subprocess
import os

##EX4
class subtitles:
    def __init__(self, video_path, subtitles_path):
        self.video_path = video_path
        self.subtitles_path = subtitles_path

    def integrate_subtitles(self, output_path):
        command = f'ffmpeg -i {self.video_path} -vf "subtitles={self.subtitles_path}" {output_path}'
        subprocess.run(command, shell=True, check=True)

##EXAMPLE
video_processor = subtitles('/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/Semi2/Big_Buck_Bunny.mp4', '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/Semi2/Toy Story (1995).srt')
#Integrate the subtitles into the video and save it 
video_processor.integrate_subtitles('EX_4_video_with_subtitles.mp4')

