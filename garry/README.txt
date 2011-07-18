Чтобы запустить

Ставим frontik на CentOS

Удостоверьтесь что у вас прописан epel

$ cat /etc/yum.repos.d/epel.repo
[epel]
name=Extra Packages for Enterprise Linux 5 - $basearch
#baseurl=http://download.fedoraproject.org/pub/epel/5/$basearch
mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=epel-5&arch=$basearch
failovermethod=priority
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL

[epel-debuginfo]
name=Extra Packages for Enterprise Linux 5 - $basearch - Debug
#baseurl=http://download.fedoraproject.org/pub/epel/5/$basearch/debug
mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=epel-debug-5&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL
gpgcheck=1

[epel-source]
name=Extra Packages for Enterprise Linux 5 - $basearch - Source
#baseurl=http://download.fedoraproject.org/pub/epel/5/SRPMS
mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=epel-source-5&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL
gpgcheck=1

Обновляем питон:
sudo yum install python26.i386 python26-devel.i386 gcc.x86_64

Делаем питон 2.6 питоном по умолчанию:
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python26 /usr/bin/python

Чиним yum (который сломался после предыдущего шага):
sudo sed -i -e 's/python/python2.4/' /usr/bin/yum

Ставим пакеты для питона:
sudo yum install python-lxml.i386 python-daemon.noarch

Перемещаем пакеты из питона 2.4 в питон 2.6 (в нашем репозитории нет этих пакетов для питона 2.6):
sudo cp -vr /usr/lib/python2.4/site-packages/lxml* /usr/lib/python2.6/site-packages/
sudo cp -vr /usr/lib/python2.4/site-packages/daemon /usr/lib/python2.6/site-packages/

Ставим curl (http://curl.haxx.se/):
wget http://curl.haxx.se/download/curl-7.21.7.tar.gz
tar xvfz curl-7.21.7.tar.gz
cd curl-7.21.7
./configure
make
sudo make install

Ставим pycurl (http://pycurl.sourceforge.net/download/):
wget http://pycurl.sourceforge.net/download/pycurl-7.19.0.tar.gz
tar xvfz pycurl-7.19.0.tar.gz
cd pycurl-7.19.0
python setup.py build
sudo python setup.py install

Делаем симлинк на новую библиотеку (если нужно):
ln -s /usr/local/lib/libcurl.so.4 /usr/lib/

Ставим setup tools
sudo yum install python26-setuptools

Ставим tornado-util (https://github.com/hhru/tornado-util):
git clone https://github.com/hhru/tornado-util.git
cd tornado-util
python setup.py build
sudo python setup.py install

Ставим tornado (https://github.com/hhru/tornado):
git clone https://github.com/hhru/tornado.git
cd tornado
python setup.py build
sudo python setup.py install

Ставим frontik (https://github.com/hhru/frontik):
git clone https://github.com/hhru/frontik.git
cd frontik
python setup.py build
sudo python setup.py install


Ставим Rubby
wget ftp://ftp.ruby-lang.org//pub/ruby/1.9/ruby-1.9.2-p0.tar.gz
tar xzvf ruby-1.9.2-p0.tar.gz
yum groupinstall ‘Development Tools’
yum install readline-devel
cd ruby-1.9.2-p0
./configure
make
sudo make install

Ставим SASS
gem install sass 

Выкачиваем application garry.
Важно чтобы garry был в pythonpath, я для этого использовал virtualenv

Копируем config.cfg.ex в config.cfg
Прописываем путь к статике.

У меня статику раздает nginx на этойже машине
Настраиваем nginx так чтобы он раздавал статику и направлял запросы на frontik.
Вот мой пример конфига
     server {
         listen  localhost:80;
         location /static {
             root /home/user/.virtualenvs/garry/application/garry/;
         }
         location / {
             proxy_pass http://localhost:9300/garry/;
         }
     }

Указываем SASS конвертировать CSS
sass --watch markup:markup

В конфиге к frontik /etc/frontik/frontik.cfg указать путь к application
urls = [
    (r".*",                     App("garry", "/home/user/.virtualenvs/garry/application/garry/garry") )
]

