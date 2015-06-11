"""
Unit tests runner for any ``django`` project.
Tests are independent from this example application but setuptools need
instructions how to interpret ``test`` command when we run::

    python setup.py test

"""
import os
import sys
import django
import testconf.settings as settings

from django.core.exceptions import ImproperlyConfigured

os.environ["DJANGO_SETTINGS_MODULE"] = settings.__name__


def run_tests(settings):
    """
    Runs tests for all the apps in testconf.settings.TEST_APPS

    """
    if hasattr(django, 'setup'):
        django.setup()

    # can only be imported after django is configured
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_runner = TestRunner(interactive=False)
    try:
        TEST_APPS = settings.TEST_APPS
    except:
        raise ImproperlyConfigured(
            (
                '[ERROR] Your test settings "%s" ' +
                'should define which apps to test' +
                ' in TEST_APP setting'
            ) %
            (settings.__name__)
        )

    # As we use different TestRunners for django < 1.8 and >= 1.8
    # the arguments run_tests differs
    if django.VERSION < (1, 8):
        # in django<1.8 we use only the last part of the module path
        # e.g. auth
        test_apps = [x.split('.')[-1] for x in TEST_APPS]
    else:
        # in django>1.8 we use full module paths
        # e.g. django.contrib.auth
        test_apps = TEST_APPS

    failures = test_runner.run_tests(test_apps)

    return failures


def main():
    failures = run_tests(settings)
    sys.exit(failures)

if __name__ == '__main__':
    main()
