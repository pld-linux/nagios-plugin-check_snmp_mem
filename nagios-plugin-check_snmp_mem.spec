%define		plugin	check_snmp_mem
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check system memory via SNMP
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania poprzez SNMP wykorzystania pamięci RAM i SWAP
Name:		nagios-plugin-%{plugin}
Version:	0.9
Release:	2
License:	GPL
Group:		Networking
Source0:	http://www.manubulon.com/nagios/check_snmp_mem.pl
Patch0:		%{name}-path.patch
# Source0-md5:	2b59e64724735eb5f4893b36c8057679
URL:		http://www.manubulon.com/nagios/snmp_mem.html
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
Requires:	nagios-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins
%define		_noautoreq 'perl(utils)'

%description
Checks by SNMP RAM or SWAP memory usage (Linux/Unix, Cisco, Pix, HP
Procurve).

%description -l pl.UTF-8
Ta wtyczka sprawdza poprzez SNMP wykorzystanie pamieci RAM i SWAP w
systemach Linux/Unix, Cisco, HP Procurve.

%prep
%setup -q -c -T
install %{SOURCE0} .
%patch0 -p1
%{__sed} -i -e 's,@plugindir@,%{plugindir},' %{plugin}.pl

cat > nagios.cfg <<'EOF'
# Usage:
# %{plugin}!ARGUMENTS...
define command {
	command_name    %{plugin}
	command_line    %{plugindir}/%{plugin} -H $HOSTADDRESS$ $ARG1$
}
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin}.pl $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -a nagios.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
