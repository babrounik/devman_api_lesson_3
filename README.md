# Bitly url shorterer

This script gets a link. If it is a bitly link then it returns amount of clicks. It it is an usual link then it returns
shorted link.

## How to run script

You have to replace INSERT_YOUR_VALUE with your private credentials.

```
brew update $ brew install pyenv
brew update && brew upgrade pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.zshrc
source ~/.zshrc
pyenv intall 3.9.11
pyenv rehash
mkdir ~/projects/devman_api_lesson_3
cd ~/projects/devman_api_lesson_3
pyenv local 3.9.11
pip3 install pipenv
pipenv shell $(which python3)
git clone https://github.com/babrounik/devman_api_lesson_3.git
pipenv install -r requirements.txt
echo 'export BITLY_TOKEN=INSERT_YOUR_VALUE' >> ./.env
echo 'export CUSTOM_DOMAIN=INSERT_YOUR_VALUE' >> ./.env
python3 main.py
```
### Examples

#### How to short link:
```
python main.py -l https://google.com
```
![script started](https://github.com/babrounik/devman_api_lesson_3/blob/main/img/example_get_shorten.jpg?raw=true)
#### How to get clicks:
```
python main.py -l bit.ly/2CCtscC
```
![script started](https://github.com/babrounik/devman_api_lesson_3/blob/main/img/example_get_clicks.jpg?raw=true)