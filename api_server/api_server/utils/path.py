from .random import timestamp_random_base64, random_unique_uint32_generator
from django.utils.timezone import now
from django.conf import settings
from pathlib import Path

_MAX_RETRY = 10


class TooManySubDirs(ValueError):
    pass


def _add_slashes(s, count=1, group_len=1):
    r = ''
    buffer = ''
    n = 0
    for c in s:
        buffer += c
        if len(buffer) == group_len and n < count:
            n += 1
            r += buffer + '/'
            buffer = ''
    return r + buffer


def get_timestamp_random_media_filename(filename,
                                        upload_to=None,
                                        relative=True,
                                        default_suffix='',
                                        root=settings.MEDIA_ROOT,
                                        starting_sub_dirs_count=0):
    if starting_sub_dirs_count > 15:
        raise TooManySubDirs('Maximum allowed starting_sub_dirs_count is 15')
    file_path = Path(filename)
    prefix_path = Path(root)
    if upload_to is not None:
        prefix_path /= upload_to
    suffix = file_path.suffix or default_suffix
    random_generator = random_unique_uint32_generator()
    timestamp = round(now().timestamp())
    retry = 0
    path = None
    while retry < _MAX_RETRY:
        retry += 1
        random_part = next(random_generator)
        random_base64 = timestamp_random_base64(True, random_part, timestamp)
        relative_path = Path(_add_slashes(random_base64, starting_sub_dirs_count) + suffix)
        absolute_path = prefix_path / relative_path
        if not absolute_path.exists():
            if relative:
                path = relative_path
                if upload_to:
                    path = upload_to / path
            else:
                path = absolute_path
            break
    return path
