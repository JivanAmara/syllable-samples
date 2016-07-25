'''
Created on Jul 25, 2016

Creates fixtures/initial.json to populate model "SyllableSample" based on the
audio sample files found under static/syllable_samples/.

@author: jivan
'''
import os, sys, django

# --- Set up django so models can be used in this script
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'script_settings'
django.setup()

from django.conf import settings
from django.core.management.commands.migrate import call_command
from syllable_samples.models import SyllableSample

def populate_syllablesample():
    # Directory containing audio samples
    DIRPATH = os.path.join(os.path.dirname(__file__), 'static/syllable_samples')

    new_syllablesamples = []

    filenames = os.listdir(DIRPATH)
    for filename in filenames:
        path = os.path.join('static/syllable_samples', filename)
        # Without the extension
        name_only = filename.split('.')[0]
        sound = name_only[:-1]
        tone = name_only[-1]
        display = '{}{}'.format(sound, tone)
        ss = SyllableSample(path=path, sound=sound, tone=tone, display=display)
        new_syllablesamples.append(ss)

    SyllableSample.objects.bulk_create(new_syllablesamples)

if __name__ == '__main__':
    os.unlink(settings.DBPATH)
    call_command('makemigrations', 'syllable_samples')
    call_command('migrate')
    populate_syllablesample()
    with open(os.path.join(PROJECT_PATH, 'syllable_samples/fixtures/initial.json'), 'w') as fixture:
        real_stdout = sys.stdout
        sys.stdout = fixture
        call_command('dumpdata', 'syllable_samples')
        sys.stdout = real_stdout
