#!/usr/bin/env python
import sys
from pylab import *
import wave

def wf_spectr(speech):
    spf = wave.open(speech,'r')
    sound_info = spf.readframes(-1)
    sound_info = fromstring(sound_info, 'int32')

    f = spf.getframerate()

    subplot(211)
    plot(sound_info)
    title('Wave from and spectrogram of %s' % sys.argv[1])

    subplot(212)
    spectrogram = specgram(sound_info, Fs = f, scale_by_freq=True,sides='default')

    show()
    spf.close()

fil = sys.argv[1]
wf_spectr(fil)
