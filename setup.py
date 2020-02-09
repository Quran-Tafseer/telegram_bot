from setuptools import setup

setup(
    name='quran_telegram_bot',
    version='0.1',
    packages=['quran_tafseer_bot'],
    url='http://api.quran-tafseer.com',
    license='',
    author='emadmokhtar',
    author_email='emad.m.habib@gmail.com',
    description='Telegram bot for Quran tafseer and translations',
    entry_points={
        'console_scripts': ['quran_telegram_bot=quran_telegram_bot:main']
    }
)
