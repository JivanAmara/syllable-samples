'''
Created on Jul 25, 2016

Creates fixtures/initial.json to populate model "SyllableSample" based on the
audio sample files found under static/syllable_samples/.

@author: jivan
'''
import os, sys, django

from django.conf import settings
from django.core.management import call_command
from hanzi_basics.pinyin_nums_to_markers import num_to_tone
from io import StringIO
import codecs

# --- Set up django so models can be used in this script
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'script_settings'
django.setup()
from syllable_samples.models import SyllableSample


def populate_syllablesample():
    # Directory containing audio samples
    DIRPATH = os.path.join(os.path.dirname(__file__), 'static/syllable_samples')

    new_syllablesamples = []

    filenames = os.listdir(DIRPATH)
    for filename in filenames:
        path = os.path.join('syllable_samples', filename)
        # Without the extension
        name_only = filename.split('.')[0]
        sound = name_only[:-1]
        tone = name_only[-1]
        display = num_to_tone('{}{}'.format(sound, tone))
        ss = SyllableSample(path=path, sound=sound, tone=tone, display=display)
        new_syllablesamples.append(ss)

    SyllableSample.objects.bulk_create(new_syllablesamples)

if __name__ == '__main__':
    # Delete the database in case it already exists and has dated data in it.
    try:
        os.unlink(settings.DBPATH)
    except:
        pass

    # Empty the current intial_data.json
    with open(os.path.join(PROJECT_PATH, 'syllable_samples/fixtures/initial_data.json'), 'w') as fixture:
        fixture.write('[]')

    call_command('makemigrations', 'syllable_samples')
    call_command('migrate')
    SyllableSample.objects.all().delete()
    populate_syllablesample()

    # --- Dump the new table to an ascii-encoded fixture
    uft8_fixure_filepath = os.path.join(PROJECT_PATH, 'syllable_samples/fixtures/initial_data.json.utf8')
    with open(uft8_fixure_filepath, 'w') as utf8_fixture:
        real_stdout = sys.stdout
        sys.stdout = utf8_fixture
        call_command('dumpdata', 'syllable_samples')

    ascii_content = \
        codecs.open(uft8_fixure_filepath, 'r', 'utf8').read().encode('ascii', 'backslashreplace')
    os.unlink(uft8_fixure_filepath)

    with open(os.path.join(PROJECT_PATH, 'syllable_samples/fixtures/initial_data.json'), 'wb') as ascii_fixture:
        ascii_fixture.write(ascii_content)
        sys.stdout = real_stdout
        print('updated syllable_samples/fixtures/initial_data.json to match audio files in static/')
