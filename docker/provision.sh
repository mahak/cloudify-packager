echo bootstrapping...

# update
echo updating apt cache
sudo apt-get -y update &&

# install prereqs
echo installing prerequisites
sudo apt-get install -y curl python-dev vim git

sudo apt-get install linux-image-generic-lts-raring linux-headers-generic-lts-raring
[ -e /usr/lib/apt/methods/https ] || {
  apt-get update
  apt-get install apt-transport-https
}
curl -sSL https://get.docker.io/ubuntu/ | sudo sh
# sudo docker run -i -t ubuntu /bin/bash


# install pip
curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python

# go home
cd ~

# virtualenv
echo installing virtualenv
sudo pip install virtualenv==1.11.4 &&
echo creating cloudify virtualenv
virtualenv cloudify &&
source cloudify/bin/activate &&

echo bootstrap done.