from setuptools import setup, find_packages

setup(
    name='sintegraIEValidator',
    version='0.1.5',  # Atualização da versão
    packages=find_packages(),
    license='MIT',
    description='Um validador de inscrição estadual para estados brasileiros.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Seu Nome',
    author_email='seuemail@example.com',
    url='https://github.com/seuusuario/validadorie',
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='validação inscrição estadual brasil estados',
)

