# 必要なライブラリをインストール
sudo yum -y update
sudo yum -y install git gcc gcc-c++ make openssl-devel bzip2-devel zlib-devel readline-devel sqlite-devel

# pyenvをインストールして設定
git clone https://github.com/yyuu/pyenv.git ~/.pyenv

echo -e '
# pyenv environment
export PYENV_ROOT="${HOME}/.pyenv"
if [ -d "${PYENV_ROOT}" ]; then
export PATH=${PYENV_ROOT}/bin:$PATH
eval "$(pyenv init -)"
fi' >> ~/.bash_profile

source ~/.bash_profile
pyenv install 3.6.5

# インストール済みリストと現在のバージョンを確認する
pyenv versions
pyenv global 3.6.5
pip install --upgrade pip

# クローリングで使うライブラリをインストール
pip install scrapy
pip install requests

# プロジェクトを作成
scrapy startproject example
cd example/
# spiderを作成
scrapy genspider examplespider www.yahoo.co.jp
# テスト実行
scrapy crawl examplespider
