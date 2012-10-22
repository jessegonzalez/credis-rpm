Name:		credis	
Version:	0.2.3
Release:	1%{?dist}
Summary:	C Client library for Redis.
Group:		Development/Libraries
License:	New BSD (no advertising, 3 clause)
URL:		http://code.google.com/p/credis/
Source0:	http://credis.googlecode.com/files/credis-0.2.3.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Packager:	Jesse Gonzalez <jesse.gonzalez@rackspace.com>

%description 
Credis is a client library in plain C for communicating with Redis servers.
Redis is a high performance key-value database, refer to Redis project page
for more information.

Credis aims to be fast and minimalistic with respect to memory usage. It
supports connections to multiple Redis servers. It runs on Linux, OS X,
Windows, FreeBSD and should run on most POSIX like systems. It is released
under the New BSD License.

Static and dynamic libraries for credis.

%package devel
Summary:	Header files for credis

%description devel
Header files for credis.

%prep
%setup -q

%build
make %{?_smp_mflags}
strip libcredis.so

%install
rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}%{_includedir}
install -m 755 -d %{buildroot}%{_libdir}

cp credis-test %{buildroot}%{_bindir}
cp credis.h %{buildroot}%{_includedir}
cp libcredis.so %{buildroot}%{_libdir}/libcredis.so.%{version}
cp libcredis.a %{buildroot}%{_libdir}

cd %{buildroot}%{_libdir}
ln -s libcredis.so.%{version} libcredis.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/credis-test
%{_libdir}

%files devel
%defattr(-,root,root,-)
%{_includedir}

%changelog
* Sat Oct 20 2012 Jesse Gonzalez <jesse.gonzalez@rackspace.com> - 0.2.3-1
Initial packaging of credis and credis-devel.
