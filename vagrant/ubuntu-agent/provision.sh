
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

# install virtualenv
sudo pip install virtualenv==1.11.4 &&

# install packman
sudo pip install https://github.com/cloudify-cosmo/packman/archive/develop.tar.gz

# create cloudify components package
cd /cloudify-packager/ &&

# LIMOR, PLEASE COMPLETE THE GET PROCESS HERE

sudo pkm pack -c linux-agent
sudo pkm pack -c cloudify-ubuntu-agent
sudo mkdir /cloudify-packager/output-packages
sudo mv /cloudify/* /cloudify-packager/output-packages

echo bootstrap done
echo NOTE: currently, using some of the packman's features requires that it's run as sudo.
