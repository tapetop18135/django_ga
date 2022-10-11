from distutils.core import setup

setup(name='django_ga',
      version='0.1',
      description='A simple Django application to integrate Google Analytics',
      author='Nuttakit Kutparb',
      author_email='a5810032@gmail.com',
      url='https://github.com/tapetop18135/django_ga/tree/main',
      packages=['google_analytics','google_analytics.templatetags',],
      package_data={'google_analytics': ['templates/google_analytics/*.html']},
      keywords=['python', 'ga', 'google', 'analytics', 'django', 'template', 'tag'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )