import os

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages


my_project_path = os.path.abspath(os.path.dirname(__file__))

long_description = """
    The program readout digital meter images from edgeAI devices, collect the images 
    and removes duplicated.
    The images will be anonymized (name replaced with hash).
    At last step, the images will be pre labeled by a neuronal network
    """

setup(
    name='collectmeteranalog',
    version='1.0.1',
    url='https://github.com/haverland/collectmeteranalog',
    license='Apache 2.0',
    author='Frank Haverland',
    author_email='iotson@t-online.de',
    include_package_data=True,
    install_requires=['pillow',
                    'numpy',
                    'matplotlib',
                    'scipy',
                    'scikit-learn',
                    'imagehash',
                    'urllib3',
                    'requests',
                    'pandas',
                    'tflite-runtime; sys_platform == "linux"',
                    'importlib-metadata; python_version == "3.9"'],
    tests_require=['nose'],
    packages=find_packages(exclude=['tests']),
    description='Reads images from water meter pointers.',
    long_description = long_description,
    platforms='any',
    keywords = "different tags here",
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    package_data={'collectmeteranalog': ['models/*.tflite']},

    )