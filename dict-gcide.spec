%define		dictname gcide
Summary:	Collaborative International Dictionary of English for dictd
Summary(pl.UTF-8):	Słownik Collaborative International Dictionary of English dla dictd
Name:		dict-%{dictname}
Version:	0.44
Release:	4
License:	GPL
Group:		Applications/Dictionaries
Source0:	ftp://ftp.dict.org/pub/dict/pre/%{name}-%{version}.tar.gz
# Source0-md5:	641502e6fedca32cbf9777b1f4f76afe
# based on ftp://ftp.gnu.org/gnu/gcide/gcide-0.46/README.DIC
Source1:	%{name}-README.DIC
URL:		http://www.dict.org/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	%{_sysconfdir}/dictd
Requires:	dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains GCIDE (Collaborative International Dictionary of
English) %{version} formatted for use by the dictionary server in the
dictd package.

%description -l pl.UTF-8
Ten pakiet zawiera słownik GCIDE (Collaborative International
Dictionary of English) %{version} sformatowany do używania z serwerem
słownika dictd.

%prep
%setup -c -q
install %{SOURCE1} README.DIC

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd,%{_sysconfdir}/dictd}

dictprefix=%{_datadir}/dictd/%{dictname}
echo "# Collaborative International Dictionary of English (%{version})
database %{dictname} {
	data  \"$dictprefix.dict.dz\"
	index \"$dictprefix.index\"
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}.dictconf
cp -a %{dictname}.* $RPM_BUILD_ROOT%{_datadir}/dictd

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q dictd restart

%postun
if [ "$1" = 0 ]; then
	%service -q dictd restart
fi

%files
%defattr(644,root,root,755)
%doc README.DIC
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}.dictconf
%{_datadir}/dictd/%{dictname}.*
