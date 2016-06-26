# `ffmpeg.c` is a program in C. Your goal is to add line number to 
# each line without disrupting their identation.
# For example:
#
# `   1  /*"`
# .
# .
# .
# `  26  #include "config.h"`
# `  27  #include <ctype.h>`
# .
# .
# .
# ` 169  static int sub2video_get_blank_frame(InputStream *ist)`
# ` 170  {`
# Output the result to `ffmpegNumbered.c`.
#

# Your program here.

f= open('ffmpeg.c','r')
w= open('test2.py','w')
i=1
for line in f:

    w.write(str(i)+line)

    i+=1
f.close()
