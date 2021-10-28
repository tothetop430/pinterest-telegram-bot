from distutils.core import setup

setup(
    name="pinterest-telegram-bot",
    version="5.3.0",
    author="Dineshkarthik Raveendran",
    author_email="hello@dineshkarthik.me",
    description="A simple script to download media from telegram",
    url="https://github.com/Dineshkarthik/pinterest-telegram-bot",
    download_url="https://github.com/Dineshkarthik/pinterest-telegram-bot/releases/latest",
    py_modules=["pinterest_telegram_bot"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
    ],
    project_urls={
        "Tracker": "https://github.com/Dineshkarthik/pinterest-telegram-bot/issues",
        "Community": "https://t.me/joinchat/Fw-oXxjOcKcuhIHt",
        "Source": "https://github.com/Dineshkarthik/pinterest-telegram-bot",
    },
    python_requires=">=3.6",
)
