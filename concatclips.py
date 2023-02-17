import os

# Get the absolute path of the directory that the Python file is in
dir_path = os.path.dirname(os.path.abspath(__file__))

#Renames the clips because ffmpeg has name requirements
def main():
    
    for count, file_name in enumerate(os.listdir(dir_path)):
        #Checks for video files with .mkv extension (might not work with other formats though there is no reason it shouldn't)
        if file_name.endswith(".mkv"):
            dst = f"clip{str(count)}.mkv"
            src =f"{dir_path}/{file_name}"
            dst =f"{dir_path}/{dst}"
            
            # rename() function will rename all the files
            os.rename(src, dst)

# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()
 
# Open the output file in write mode
with open("output.txt", "w") as output_file:
    # Iterate over all files in the directory
    for file_name in sorted(os.listdir(dir_path)):
        # Check if the file has a .mkv extension
        if file_name.endswith(".mkv"):
            # Write the file name to the output file
            output_file.write('file \'' + file_name + '\'\n')   # writen like:     file 'clip1.mkv'

# Command to combine clips/videos in the output.txt file which contains all renamed clips
cmd = "ffmpeg -f concat -i output.txt -c copy output.mp4"
os.system(cmd)
