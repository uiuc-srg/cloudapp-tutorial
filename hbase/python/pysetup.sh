#!/bin/bash

yum install -y nano centos-release-SCL zlib-devel \
bzip2-devel openssl-devel ncurses-devel \
sqlite-devel readline-devel tk-devel \
gdbm-devel db4-devel libpcap-devel xz-devel \
libpng-devel libjpg-devel atlas-devel

yum groupinstall "Development tools" -y

yum install -y python27

echo "#!/bin/bash
source /opt/rh/python27/enable" > /etc/profile.d/enablepython27.sh
