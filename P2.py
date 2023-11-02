import subprocess
import json


input_file_path = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/Big_Buck_Bunny.mp4'

##EX1
output  = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/Big_Buck_Bunny_EX1.mpg'
cmd = f"ffmpeg -i {input_file_path} {output}"

#Run the ffmpeg command to convert MP4 to MP2
subprocess.run(cmd, shell=True, check=True)
print(f'Conversion complete. MP2 file saved at: {output}')


##EX2
def modify_resolution(input_video_path, output_video_path, width, height):
    try:
        # Run ffmpeg command to modify the resolution
        ffmpeg_command = f'ffmpeg -i {input_video_path} -vf "scale={width}:{height}" -c:a copy {output_video_path}'
        subprocess.run(ffmpeg_command, shell=True, check=True)
        print(f'Resolution modified. Modified video saved at: {output_video_path}')
    except subprocess.CalledProcessError as e:
        print(f'Error occurred: {e}')

###Doing it with our video
output = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/Big_Buck_Bunny_modified_EX2.mp4'
width = 640  #width of the output video
height = 480  #Height of the output video
modify_resolution(input_file_path, output, width, height)

##EX3
def change_chroma_subsampling(input_video_path, output_video_path, chroma_subsampling):
    try:
        #Run ffmpeg command to change chroma subsampling
        ffmpeg_command = f'ffmpeg -i {input_video_path} -c:v libx264 -vf format={chroma_subsampling} {output_video_path}'
        subprocess.run(ffmpeg_command, shell=True, check=True)
        print(f'Chroma subsampling changed. Modified video saved at: {output_video_path}')
    except subprocess.CalledProcessError as e:
        print(f'Error occurred: {e}')

###Doing it with our video
output = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/Big_Buck_Bunny_subsampling_EX3.mp4'
chroma_subsampling = 'yuv420p'  # Desired chroma subsampling format

change_chroma_subsampling(input_file_path, output, chroma_subsampling)


##EX4
def get_video_info(input_video_path):
    try:
        #Run ffprobe command to get video information
        ffprobe_command = f'ffprobe -v quiet -print_format json -show_streams -select_streams v:0 {input_video_path}'
        result = subprocess.run(ffprobe_command, shell=True, check=True, stdout=subprocess.PIPE, text=True)

        #Parse the JSON output
        video_info = json.loads(result.stdout)

        #Return video information
        return video_info
    except subprocess.CalledProcessError as e:
        print(f'Error occurred: {e}')
        return None

def print_video_info(video_info):

    if video_info:
        print('Video Information:')
        print(f'Codec: {video_info["streams"][0]["codec_name"]}')
        print(f'Resolution: {video_info["streams"][0]["width"]}x{video_info["streams"][0]["height"]}')
        print(f'Frame Rate: {eval(video_info["streams"][0]["r_frame_rate"])} fps')
        print(f'Duration: {video_info["streams"][0]["duration"]} seconds')
        print(f'Bitrate: {int(video_info["streams"][0]["bit_rate"])/1000} kbps')
    else:
        print('Failed to retrieve video information.')

##Print relevant data of our video
print_video_info(get_video_info(input_file_path))


##EX5
import sys
sys.path.append('/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid')  # Add the path to the directory containing rgb_yuv.py

from rgb_yuv import *
rgb_values = (255, 0, 0)  
print("RGB to YUV:", rgb_to_yuv(*rgb_values))

