%define		dictname gcide
Summary:	Collaborative International Dictionary of English for dictd
Summary(pl):	S³ownik Collaborative International Dictionary of English dla dictd
Name:		dict-%{dictname}
Version:	0.44
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	ftp://ftp.dict.org/pub/dict/pre/%{name}-%{version}.tar.gz
# based on ftp://ftp.gnu.org/gnu/gcide/gcide-0.46/README.DIC
Source1:	%{name}-README.DIC
URL:		http://www.dict.org/
Requires:	dictd
Requires:	%{_sysconfdir}/dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains GCIDE (Collaborative International Dictionary of
English) %version formatted for use by the dictionary server in the
dictd package.

%description -l pl
Ten pakiet zawiera s³ownik GCIDE (Collaborative International
Dictionary of English) %version sformatowany do u¿ywania z serwerem
s³ownika dictd.

%prep
%setup -c -q
install %{SOURCE1} README.DIC

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd,%{_sysconfdir}/dictd}

dictprefix=%{_datadir}/dictd/%{dictname}
echo "# Collaborative International Dictionary of English (%version)
database %{dictname} {
	data  \"$dictprefix.dict.dz\"
	index \"$dictprefix.index\"
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}.dictconf
mv %{dictname}.* $RPM_BUILD_ROOT%{_datadir}/dictd

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%files
%defattr(644,root,root,755)
%doc README.DIC
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}.dictconf
%{_datadir}/dictd/%{dictname}.*
