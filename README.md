# Bitly URL shortener

This project helps to shorten URL links (generate bitlinks) and to get clicks for already shortened links (bitlinks) by using [Bitly - URL shortening service and a link management platform](https://bitly.com/).


### How to install:

1. Firstly you have to install python and pip (package-management system) if it hasn't been already installed.

2. Create virtual enviorment with its own independent set of packages using [virtualenv/venv](https://docs.python.org/3/library/venv.html). It'll help you to isolate the project from the packages located in the base enviornment.

3. Install all of the packages used in this project, in your virtual enviorment which you've created on the step 2. Use the `requirements.txt` file to install packages:
    ```console
    pip install -r requirements.txt
    ```
4. Also you need to create an account on [bitly.com](https://bitly.com/) and generate your own [access token](https://app.bitly.com/settings/api/), which would be used in [The Bitly API](https://dev.bitly.com/).

5. Creat an `.env` file and locate it in te same directory where your project and `main.py` file are. Copy and and append your access token to `.env` file like this:
    ```
    BITLY_TOKEN=paste_here_your_token_from_step_5
    ```
6. Don't forget to add `.env` to your `.gitignore` if you are going to put project on GIT.


### How to use

- Shortening URL:
```console
>>> root@ubuntu:~$ main.py https://www.google.com/
Your shortened link for https://www.google.com/ is: https://bit.ly/3asd3esv
```

- Getting count of clicks for bitlink:
```console
>>> root@ubuntu:~$ main.py https://bit.ly/3asd3esv
Count of clicks on https://bit.ly/3asd3esv is: 0
```

### Project Goals

This code was written for educational purposes.
