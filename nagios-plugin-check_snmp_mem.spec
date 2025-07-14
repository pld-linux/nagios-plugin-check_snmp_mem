%define		plugin	check_snmp_mem
Summary:	Nagios plugin to check system memory via SNMP
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania poprzez SNMP wykorzystania pamięci RAM i SWAP
Name:		nagios-plugin-%{plugin}
Version:	1.1
Release:	2
License:	GPL
Group:		Networking
Source0:	http://nagios.proy.org/check_snmp_mem.pl
# Source0-md5:	f4b03cf520e6e4eab9dc6a67c88032d9
Patch0:		%{name}-path.patch
Patch1:		net-snmp-version.patch
Patch2:		noswap-critical.patch
Source1:	%{plugin}.cfg
URL:		http://nagios.proy.org/snmp_mem.html
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	sed >= 4.0
Requires:	nagios-core
Requires:	perl-Net-SNMP >= 5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%define		_noautoreq_perl utils

%description
Checks by SNMP RAM or SWAP memory usage (Linux/Unix, Cisco, Pix, HP
Procurve).

%description -l pl.UTF-8
Ta wtyczka sprawdza poprzez SNMP wykorzystanie pamieci RAM i SWAP w
systemach Linux/Unix, Cisco, HP Procurve.

%prep
%setup -qcT
install -p %{SOURCE0} .
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%{__sed} -i -e 's,@plugindir@,%{plugindir},' %{plugin}.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin}.pl $RPM_BUILD_ROOT%{plugindir}/%{plugin}
%{__sed} -e 's,@plugindir@,%{plugindir},' %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
