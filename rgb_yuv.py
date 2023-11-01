import subprocess
import numpy as np
from scipy.fftpack import dct, idct
from PIL import Image
##EX1 
def rgb_to_yuv(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = 0.492 * (b - y)
    v = 0.877 * (r - y)
    return y, u, v

def yuv_to_rgb(y, u, v):
    r = y + 1.14 * v
    g = y - 0.395 * u - 0.581 * v
    b = y + 2.032 * u
    return r, g, b

#Example of EX1
rgb_values = (255, 0, 0)  
print("RGB to YUV:", rgb_to_yuv(*rgb_values))
yuv_values = rgb_to_yuv(*rgb_values)
print("YUV to RGB:", yuv_to_rgb(*yuv_values))

##EX2
def resize_and_convert_image(input_file, output_file, width, height):
    #Resize the image using FFmpeg command
    ffmpeg_command = f'ffmpeg -i {input_file} -vf "scale={width}:{height}" {output_file}'
    subprocess.run(ffmpeg_command, shell=True)

#Example of EX2
input_image = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/siscod_lab1.jpeg'  # Full path to the input image file
output_image = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/resized.jpeg'  # Path to the resized output image file
new_width = 320  #New width of the image
new_height = 240  #New height of the image
resize_and_convert_image(input_image, output_image, new_width, new_height)


##EX3
def serpentine(file_path):
    serpentine_bytes = []
    with open(file_path, 'rb') as file:
        #First of all, we have to read all bytes from the file
        image_bytes = file.read()
        
        # Read the bytes in a serpentine (zigzag) pattern
        width, height = 0, 0
        for byte in image_bytes:
            #We have to append the byte to the serpentine_bytes list
            serpentine_bytes.append(byte)
            
            #Checking if the current position is at the end of the row
            if height % 2 == 0:
                width += 1
            else:
                width -= 1
            
            #Checking if the current position is at the end of the image width
            if width >= 640:  #Assuming width of the image is 640 for example
                height += 1
                width -= 1
            elif width < 0:
                height += 1
                width += 1
        
    return bytes(serpentine_bytes)

#Example of EX3
print(serpentine(input_image))


##EX4 
def compress_to_bw(input_image, output_image, quality=0):
    command = [
            'ffmpeg',
            '-i', input_image,
            '-vf', 'format=gray',
            '-q:v', str(quality),
            output_image
        ]
    subprocess.run(command, check=True)
#Example of EX4
output_image = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/resizedandBW.jpeg'
compress_to_bw(input_image, output_image)




##EX5
def run_length_encode(data):
    encoded_data = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded_data.extend([data[i - 1], count])
            count = 1
    encoded_data.extend([data[-1], count])
    return bytes(encoded_data)

#Example of EX5
input_bytes = b'\x01\x01\x02\x02\x03\x03\x04\x04\x05\x05'
print("Encoded bytes:", run_length_encode(input_bytes))



##EX6
class DCTConverter:
    def _init_(self):
        pass

    def forward_dct(self, data):
        return dct(dct(data.T, norm='ortho').T, norm='ortho')

    def inverse_dct(self, encoded_data):
        return idct(idct(encoded_data.T, norm='ortho').T, norm='ortho')

#Example of EX6
#
output_image = '/Users/marina/Desktop/UNI/4rdyear/1rstTerm/CodAudioVideo/LABS_video/SisCod_Aud_Vid/reconstructed_image.jpeg'

#First of all, we need to load an image as a numpy array
image = np.array(Image.open(input_image).convert('L'))

#Create or initialize an instance of the DCTConverter class
dct_converter = DCTConverter()

#Then do the forward DCT on the image
dct_image = dct_converter.forward_dct(image)

#Later, do the inverse DCT to reconstruct the image
reconstructed_image = dct_converter.inverse_dct(dct_image)

#Then convert the reconstructed numpy array back to an image
reconstructed_image = Image.fromarray(np.uint8(reconstructed_image))

#And finally, save the reconstructed image
reconstructed_image.save(output_image)