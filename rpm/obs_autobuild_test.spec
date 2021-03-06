%define _topdir    /home/abuild/rpmbuild
%define _sourcedir %{_topdir}/SOURCES
%define _builddir  %{_topdir}/BUILD

%define logmsg logger -t %{name}/rpm

Name:          obs-autobuild-test
Version:       1.0
Release:       0.1%{?dist}
Summary:       A test to see how autobuilding works with open build services
Group:         Group/goes/here
License:       Apache2.0
URL:           https://github.com/seccubus/obs_autobuild_test
Vendor:        Frank Breedijk
Distribution:  Group for specific distribution

Source:        %{name}-%{version}.tar.gz
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
#BuildRequires: /bin/rm, /bin/mkdir, /bin/cp
#Requires:      /bin/bash, /bin/date
Requires:      perl-Digest-MD5
Requires:      perl-Data-Dumper
Requires:      perl-GetOpt-Long
BuildArch:     noarch

%description
A test to see how autobuilding works with open build services

%prep
%setup -q

%build
pwd
echo "Running compiler"
mkdir etc
touch etc/bla.txt

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 etc/bla.txt %{buildroot}/etc/bla.txt

%pre
# Pre-install steps go here.

%post
# Post-install steps go here.

%preun
# Steps prior to uninstall go here.

%postun
# Steps after uninstall go here.

%clean
%{__rm} -rf %{buildroot}

%files
%doc README.md
%defattr(-,root,root,0755)
#/list/files/here
/etc/bla.txt

%changelog

* Wed Feb 24 2016 Frank Breedijk 
- Initial version. Date format is `date +"%a %b %d %Y`. Comments go here.