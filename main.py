import os
import imageio
import subprocess as sp


def main(video_path, time_points, save_path, max_size=200):
    # Read video info using imageio
    video = imageio.get_reader(video_path, 'ffmpeg')
    width, height = video.get_meta_data().get('size')
    scale = max_size/width if width >= height else max_size/height
    if width >= height:
        new_width, new_height = max_size, int(height*scale//2*2)
    else:
        new_width, new_height = int(width*scale//2*2), max_size

    # Cut slices from the original video
    fp = open('tmp.txt', 'w')
    for i, point in enumerate(time_points):
        command = ['ffmpeg', '-y', '-ss', str(point[0]), '-to', str(point[1]),
                   '-i', video_path, '-vf', 'scale={}:{}'.format(new_width, new_height),
                   '{}.mp4'.format(i)]
        sp.call(command)
        fp.write('file {}.mp4\n'.format(i))
    fp.close()

    # Concatenate video slices into a gif
    command = ['ffmpeg', '-y', '-f', 'concat', '-i', 'tmp.txt', save_path]
    sp.call(command)

    # Remove temporary files
    with open('tmp.txt', 'r') as fp:
        for line in fp.readlines():
            os.remove(line.split()[-1])
    os.remove('tmp.txt')
    return True


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Process input parameters to generator a gif file from a video')
    parser.add_argument('-v', '--video_path', help='Video path', required=True)
    parser.add_argument('-p', '--points', help='''Points of timestamps. It should be a combination of start and 
    end points, such as 1,5:10,15''', required=True)
    parser.add_argument('-s', '--save_path', help='''Path to save the gif. If not given, the gif will be saved 
    with the input video''')
    parser.add_argument('-m', '--max_size', type=int, default=200, help='The max width/height of the generated gif')
    args = parser.parse_args()
    print(args)

    points = [point.split(',') for point in args.points.split(':')]
    save_path = args.save_path if args.save_path else '{}.gif'.format(os.path.splitext(args.video_path)[0])
    main(video_path=args.video_path, time_points=points, max_size=args.max_size//2*2, save_path=save_path)

