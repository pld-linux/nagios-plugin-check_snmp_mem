%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check system memory via SNMP
Summary(pl.UTF-8):   Wtyczka Nagiosa do sprawdzania poprzez SNMP wykorzystania pamięci RAM i SWAP
Name:		nagios-plugin-check_snmp_mem
Version:	0.9
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.manubulon.com/nagios/check_snmp_mem.pl
Patch0:		%{name}-path.patch
# Source0-md5:	2b59e64724735eb5f4893b36c8057679
URL:		http://www.manubulon.com/nagios/snmp_mem.html
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
Requires:	nagios-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins
%define		_noautoreq 'perl(utils)'

%description
Checks by SNMP RAM or SWAP memory usage (Linux/Unix,Cisco,
Pix,HP Procurve).

%description -l pl.UTF-8
Ta wtyczka sprawdza poprzez SNMP wykorzystanie pamieci RAM i SWAP w
systemach Linux/Unix, Cisco, HP Procurve.

%prep
%setup -q -c -T
install %{SOURCE0} .
%patch0 -p1
sed -i -e 's,@plugindir@,%{_plugindir},' check_snmp_mem.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_plugindir}}
install check_snmp_mem.pl $RPM_BUILD_ROOT%{_plugindir}/check_snmp_mem.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/*
