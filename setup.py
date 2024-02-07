from setuptools import setup, find_packages

setup(
    name='no-dm-discord',
    version='0.1.0',
    author='wbnns',
    author_email='hello@wbnns.com',
    description='A Discord bot that ensures DMs are always turned off in your Discord',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wbnns/no-dm-discord',
    packages=find_packages(),
    install_requires=[
        'requests',  # Your project's dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
