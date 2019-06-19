# Gif Generator

This project is designed to generate a gif file from a given 
video and timestamps.

## Dependencies

Make sure that `imageio` and `FFMpeg` have been installed on
your computer

## Usage

The usage is quite simple. The following is an example to extract 
footage from the beginning to the fifth second and from 10th 
second to 15th second and then to generate a combined gif.
```
python3  main.py -v /path/to/test.mp4 -p 0,5:10,15
```
A gif of 10 seconds will be created in the folder in which the
test video resides. Of course, you are welcome to assign a path
to save the created gif
```
python3  main.py -v /path/to/test.mp4 -p 0,5:10,15 -s /path/to/test.gif
```
The defaulted size of the generated gif is 200 pixel. It can be
altered using parameter `-m`
```
python3  main.py -v /path/to/test.mp4 -p 0,5:10,15 -m 400
```
