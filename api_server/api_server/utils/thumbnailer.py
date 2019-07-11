from django.conf import settings
from django.utils.text import slugify


def build_thumbnail_prepend(media=settings.THUMBNAILER_DEFAULT_MEDIA,
                            variant=settings.THUMBNAILER_DEFAULT_VARIANT,
                            modifier=settings.THUMBNAILER_DEFAULT_MODIFIER):
    prepend = settings.THUMBNAILER_PREPEND
    prepend += '' if prepend.endswith('/') else '/'
    prepend += '_'.join([slugify(media) if media else '',
                         slugify(variant) if variant else '',
                         slugify(modifier) if modifier else ''])
    return prepend


def add_thumbnail_prepend_to_url(url, thumbnail_full_prepend=None,
                                 media=settings.THUMBNAILER_DEFAULT_MEDIA,
                                 variant=settings.THUMBNAILER_DEFAULT_VARIANT,
                                 modifier=settings.THUMBNAILER_DEFAULT_MODIFIER):
    thumbnail_prepend = thumbnail_full_prepend
    if not thumbnail_prepend:
        thumbnail_prepend = build_thumbnail_prepend(media, variant, modifier)
    try:
        if url.startswith('http'):
            index = url.index('/', 8)
        else:
            index = 0
    except ValueError:
        index = 0
    return url[:index] + thumbnail_prepend + url[index:]
