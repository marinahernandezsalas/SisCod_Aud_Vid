import os
from SP3 import VideoConverter
input_video_path = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/Big_Buck_Bunny.mp4'
output_directory = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/SP3'

def main():
    ##EX1

    #Create the output directory if it doesn't exist
    #os.makedirs(output_directory, exist_ok=True)

    #convert_resolution(input_video_path, output_directory, 1280, 720, 'BBB')
    #convert_resolution(input_video_path, output_directory, 854, 480, 'BBB')
    #convert_resolution(input_video_path, output_directory, 360, 240, 'BBB')
    #convert_resolution(input_video_path, output_directory, 160, 120, 'BBB')

    ##EX2
    VideoConverter.convert_resolution_and_codec(1280, 720, 'libvpx', 'BBB_720p_vp8')
    VideoConverter.convert_resolution_and_codec(1280, 720, 'libvpx-vp9', 'BBB_720p_vp9')
    VideoConverter.convert_resolution_and_codec(1280, 720, 'libx265', 'BBB_720p_h265', output_format='mp4')
    VideoConverter.convert_resolution_and_codec(1280, 720, 'libx264', 'BBB_720p_h264')



if __name__ == "__main__":
    main()
