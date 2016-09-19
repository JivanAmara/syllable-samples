'''
Created on Jul 25, 2016

@author: jivan
'''
from syllable_samples.models import SyllableSample
import random
import json

def get_random_sample():
    nsamples = SyllableSample.objects.order_by('id').count()
    s_idx = random.randint(0, nsamples - 1)
    s = SyllableSample.objects.order_by('id')[s_idx]
    hanzi = json.loads(s.hanzi_examples_json_string)
    ret = (s.sound, s.tone, s.display, s.path, hanzi)
    return ret
