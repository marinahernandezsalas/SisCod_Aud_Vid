import os
import subprocess

input_video_path = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/Big_Buck_Bunny.mp4'
output_directory = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/SP3'

def convert_resolution(input_video, output_video_dir, width, height, custom_name):
    try:
        output_video_path = os.path.join(output_video_dir, f"{custom_name}_{width}x{height}.mp4")
        subprocess.run(["ffmpeg", "-i", input_video, "-vf", f"scale={width}:{height}", "-c:a", "copy", output_video_path], check=True)
        print(f"Video converted to {width}x{height}: {output_video_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")


import os
import subprocess

class VideoConverter:
        
    def convert_resolution_and_codec(input_video,output_dir,width, height, codec, custom_name, output_format='webm'):
        output_video_path = os.path.join(output_dir, f"{custom_name}.{output_format}")
        subprocess.run(["ffmpeg", "-i", input_video, "-vf", f"scale={width}:{height}", "-c:a", "copy", "-c:v", codec, output_video_path], check=True)
        print(f"Video converted to {width}x{height} with {codec}: {output_video_path}")





