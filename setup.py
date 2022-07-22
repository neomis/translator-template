"""Setup Package."""
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(HERE, 'translator_template', '__version__.py'), 'r', encoding='utf-8') as file_handle:
    exec(file_handle.read(), about)  # pylint: disable=exec-used

with open('README.md', 'r', encoding='utf-8') as file_handle:
    readme = file_handle.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    python_requires=">=3.8",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [console_scripts]
        translate_file=translator_template.cli:translate_file
        translate_spool=translator_template.cli:translate_spool
    ''',
    install_requires=[
        'arrow',
        'click',
        'loguru',
        'pandas',
        'python-dotenv',
        'python-pidfile'
    ],
    extras_require={
        'dev': [
            'autopep8',
            'mypy',
            'pylint',
            'pylint-exit',
            'pytest',
            'pytest-cov']
    }
)
