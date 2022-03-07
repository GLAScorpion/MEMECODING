import moviepy.editor as mpy
clip = mpy.ImageSequenceClip("autism",fps=60)
clip.write_videofile("linus.mp4")
