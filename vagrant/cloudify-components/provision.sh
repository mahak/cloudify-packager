
# echo bootstrapping packman...

# update and install prereqs
sudo apt-get -y update &&
sudo apt-get install -y python-setuptools python-dev rubygems rpm libyaml-dev &&

# install ruby
wget ftp://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p547.tar.bz2
tar -xjf ruby-1.9.3-p547.tar.bz2
cd ruby-1.9.3-p547
./configure --disable-install-doc
make
sudo make install
cd ~

# install fpm and configure gem/bundler
sudo gem install fpm --no-ri --no-rdoc &&
echo -e 'gem: --no-ri --no-rdoc\ninstall: --no-rdoc --no-ri\nupdate:  --no-rdoc --no-ri' >> ~/.gemrc
echo -e 'gem: --no-ri --no-rdoc\ninstall: --no-rdoc --no-ri\nupdate:  --no-rdoc --no-ri' >> /root/.gemrc

# install pip
sudo apt-get purge pip
sudo easy_install -U pip &&
sudo wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python &&
# install pip alternative
# curl --silent --show-error --retry 5 https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | sudo python

# install virtualenv
sudo pip install virtualenv==1.11.4 &&

# install packman
sudo pip install https://github.com/cloudify-cosmo/packman/archive/develop.tar.gz

# create cloudify components package
cd /cloudify-packager/ &&
# sudo pkm make -c logstash,elasticsearch,kibana3,nginx,rabbitmq-server,riemann,nodejs,openjdk-7-jdk,virtualenv,curl,make,ruby,workflow_gems -v &&
sudo pkm make -x cloudify-components,cloudify-ui,cloudify-core,manager,celery,cloudify-ubuntu-agent,Ubuntu-agent
sudo pkm pack -c cloudify-components
sudo mkdir /cloudify-packager/output-packages
sudo mv /cloudify/* /cloudify-packager/output-packages

# TODO: add virtualenv to provisioning process
# sudo pip install virtualenvwrapper
# mkvirtualenv packman
# TODO: add bash completion support using docopt-completion
# docopt-completion #VIRTUALENV#...pkm.py?

echo bootstrap done
echo NOTE: currently, using some of the packman's features requires that it's run as sudo.