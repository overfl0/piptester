import os


def linux():
    os.environ['SPARK_VERSION'] = '3.3'
    import pydeequ  # noqa


def windows():
    os.environ['SPARK_VERSION'] = '3.3'
    import pydeequ  # noqa
