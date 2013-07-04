# To build:
# sudo yum -y install rpmdevtools && rpmdev-setuptree
# wget http://download.savannah.gnu.org/releases/libunwind/libunwind-1.1.tar.gz -O ~/rpmbuild/SOURCES/libunwind-1.1.tar.gz
# wget https://raw.github.com/nmilford/rpm-libunwind/master/libunwind.spec -O ~/rpmbuild/SPECS/libunwind.spec
# rpmbuild -bb ~/rpmbuild/SPECS/libunwind.spec

Summary:   A portable and efficient C API to determine the call-chain of a program.
Name:      libunwind
Version:   1.1
Release:   1
License:   BSD
Group:     Development/Debuggers
Source:    http://download.savannah.gnu.org/releases/libunwind/libunwind-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL:       http://savannah.nongnu.org/projects/libunwind
Conflicts: gdb < 6.6-9

%description
The primary goal of this project is to define a portable and efficient C
programming interface (API) to determine the call-chain of a program. The API
additionally provides the means to manipulate the preserved (callee-saved) state
of each call-frame and to resume execution at any point in the call-chain
(non-local goto). The API supports both local (same-process) and remote
(across-process) operation. As such, the API is useful in a number of
applications. 

%package devel
Summary: Development package for libunwind.
Group:   Development/Debuggers
Requires: %{name} = %{version}
%description devel
Libraries and header files for libunwind.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static --enable-shared
make

%makeinstall
rm -f %{buildroot}/%{_libdir}/libunwind*.la
rm -f %{buildroot}/%{_libdir}/libunwind*.a

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING README NEWS
%{_libdir}/libunwind*.so.*
%{_libdir}/pkgconfig/*.pc
%{_mandir}/*/*

%files devel
%defattr(-,root,root)
%{_libdir}/libunwind*.so
%{_includedir}/*

%changelog
* Wed Jul 03 2013 Nathan Milford <nathan@milford.io> 1.1
- Initial spec.

