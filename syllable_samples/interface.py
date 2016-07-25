'''
Created on Jul 25, 2016

@author: jivan
'''
from syllable_samples.models import SyllableSample
import random

def get_random_sample():
    nsamples = SyllableSample.objects.order_by('id').count()
    s_idx = random.randint(0, nsamples - 1)
    s = SyllableSample.objects.order_by('id')[s_idx]

    ret = (s.sound, s.tone, s.display, s.path)
    return ret
