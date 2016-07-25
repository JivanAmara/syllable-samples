SyllableSamples:
A django 1.9 app providing audio samples for many different pinyin syllables.

Dependencies:
 - Django

Typical Usage:
    import os
    from syllable_samples.interface import get_random_sample
    from django.conf import settings
    sound, tone, display, path = get_random_sample()
    sample_path = os.path.join(settings.STATIC_ROOT, path)
    sample_url = os.path.join(settings.STATIC_URL, path)

    # ...do what you need with the sample
