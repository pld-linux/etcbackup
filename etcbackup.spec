Summary:	Incremental backups of /etc
Summary(pl):	Przyrostowe kopie zapasowe /etc
Name:		etcbackup
Version:	0.1
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://team.pld.org.pl/~wolf/%{name}
Requires:	diffutils
Requires:	gzip
Requires:	tar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Incremental backups of /etc. Use at your own risk.

%description -l pl
Przyrostowe kopie zapasowe /etc. U¿ywaj na w³asn± odpowiedzialno¶æ.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/cron.hourly}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/etcbackup << EOF
#!/bin/sh
%{_bindir}/etcbackup
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sysconfdir}/cron.hourly/*
