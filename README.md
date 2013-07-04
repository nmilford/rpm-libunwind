rpm-libunwind
=============

An RPM spec file to build and install libunwind.

To build:

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`wget http://download.savannah.gnu.org/releases/libunwind/libunwind-1.1.tar.gz -O ~/rpmbuild/SOURCES/libunwind-1.1.tar.gz`

`wget https://raw.github.com/nmilford/rpm-libunwind/master/libunwind.spec -O ~/rpmbuild/SPECS/libunwind.spec`

`rpmbuild -bb ~/rpmbuild/SPECS/libunwind.spec`

