Summary:	[X]Emacs/W3 World Wide Web browser
Summary(pl.UTF-8):	Przeglądarka WWW pod [X]Emacsa
Name:		xemacs-w3-pkg
%define 	srcname	w3
Version:	1.35
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	d2e8b670e32462bb778fd32e12e16af6
Patch0:		%{name}-info.patch
URL:		http://www.xemacs.org/
BuildRequires:	texinfo
Requires:	xemacs
Requires:	xemacs-base-pkg
Requires:	xemacs-mail-lib-pkg
Conflicts:	xemacs-sumo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Emacs/W3 provides some core functionality that can be readily re-used
from any program in Emacs. Users and other package writers are
encouraged to Web-enable their applications and daily work routines
with the library.

Emacs/W3 is completely customizable, both from Emacs-Lisp and from
stylesheets. If there is any aspect of Emacs/W3 that cannot be
modified to your satisfaction, please send mail to the
w3-beta@@xemacs.org mailing list with any suggestions.

%description -l pl.UTF-8
Emacs/W3 dodaje podstawową funkcjonalność, która może być używana
przez dowolny program w Emacsie. Użytkownicy i autorzy innych pakietów
są zachęcani do @i{Web-enable} swoich aplikacji.

Emacs/W3 jest całkowicie konfigurowalny, zarówno z Emacs-Lispa jak i
styli.

%prep
%setup -q -c
%patch0 -p1

%build
cd man/w3
awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info


# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc lisp/w3/{README.VMS,README,INSTALL,ChangeLog}
%{_datadir}/xemacs-packages/etc/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%{_infodir}/*.info*
