
from setuptools import setup, find_packages

setup(
    name='sintegra-ie-validator',
    version='0.1.1',
    packages=find_packages(),
    license='MIT',
    description='Um validador de inscrição estadual para estados brasileiros, incluindo Acre e Alagoas.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='José Tiago',
    author_email='josetiagobsouza@gmail.com',
    url='https://github.com/josetiagobispo/sintegra-ie-validator',
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='validação inscrição estadual brasil estados',
)
