import ffmpeg

(
    ffmpeg
    .input('./frames/10.jpg', pattern_type='glob', framerate=25)
    .output('movie.mp4')
    .run()
)