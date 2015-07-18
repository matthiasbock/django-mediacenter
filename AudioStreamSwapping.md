## Let's do a little math ... ##

You have 2 video files, A and B, with principally same content. Now you want to watch the video, but for some reason, e.g. higher stream quality, you want to play back the video stream of A while you listen to the audio stream of B.
You could try to open two windows, one for each file, mute A and minimize B.

**Problem:**
The video playback is not synchronized to the audio playback. Sooner or later this will start to annoy you.

**Approach**:
Video A and video B are in sync with their appropriate audio streams,
so syncing the video frames will also sync the audio streams.

  1. Find two frames, showing the same content, in the beginning of the videos.
  1. Note their numbers.
  1. Do it again for another frame at the end of the videos.

From these values, you get:
  1. the relative frame shift
  1. the relative speed

With these values, you can set up e.g. _mplayer_ and do a synced playback.

## Calculation ##