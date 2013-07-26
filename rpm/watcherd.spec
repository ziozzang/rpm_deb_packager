%{!?project_release: %define project_release 1}
%{!?project_version: %define project_version master}
%{!?project_name: %define project_name project}

Summary: %{project_name}
Name: %{project_name}
Version: %{project_version}
Release: %{project_release}
License: Not Specified
Group: Applications/KTuCloud
URL: http://kt.com

Source0: %{name}-%{version}-%{release}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc
Requires(post): /sbin/chkconfig /usr/sbin/useradd
Requires(preun): /sbin/chkconfig, /sbin/service
Requires(postun): /sbin/service
Provides: ziozzang

Packager: Jioh L. Jung <ziozzang@gmail.com>

Requires: ruby, rubygems, sysstat 

%description
%{project_name}

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}

mkdir -p %{buildroot}/usr/local/watcherd
mkdir -p %{buildroot}/etc/watcherd
mkdir -p %{buildroot}/etc/watcherd/mod-available
mkdir -p %{buildroot}/etc/watcherd/mod-enabled
mkdir -p %{buildroot}/etc/init.d

%{__install} -v -Dp -m 0750 src/watcherd-bin/* %{buildroot}/usr/local/watcherd/
%{__install} -v -Dp -m 0750 src/watch.conf %{buildroot}/etc/watcherd/
%{__install} -v -Dp -m 0750 src/sample.d/* %{buildroot}/etc/watcherd/mod-available/
%{__install} -v -Dp -m 0750 src/watcherd-bin/* %{buildroot}/usr/local/watcherd/
%{__install} -v -Dp -m 0750 src/watcherd %{buildroot}/etc/init.d/
%pre

%preun
#!/bin/bash
/etc/init.d/watcherd stop
/sbin/chkconfig --del watcherd

%post
#!/bin/bash
gem install ruby-hmac
gem install daemons

/etc/init.d/watcherd start
/sbin/chkconfig --add watcherd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
/etc/init.d/watcherd
/etc/watcherd/mod-available
/etc/watcherd/mod-enabled
%config /etc/watcherd/watch.conf
%attr(600, root, root) /etc/watcherd/watch.conf
%attr(600, root, root) /usr/local/watcherd/

%changelog
* Thu Jul 25 2013 - Very first Initilzed version
- Yup.
