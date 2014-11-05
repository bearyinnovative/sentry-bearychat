try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-bearychat').version
except Exception, e:
    VERSION = 'unknown'
