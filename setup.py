import setuptools

with open('README.md') as file:
    long_description = file.read()

setuptools.setup(
    name='gravify',
    version='1.0.0',
    author='Ben Soyka',
    author_email='bensoyka@icloud.com',
    description='Simple package to generate Gravatar URLs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gravify.readthedocs.io/',
    packages=setuptools.find_packages(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=['six==1.16.0', 'validate_email==1.3'],
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    project_urls={
        'Source': 'https://github.com/bsoyka/gravify',
        'Changelog': 'https://github.com/bsoyka/gravify/releases',
    },
)
