Summary:	[X]Emacs/W3 World Wide Web browser
Summary(pl):	Przegl±darka WWW pod [X]Emacsa
Name:		xemacs-w3-pkg
%define 	srcname	w3
Version:	1.20
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		%{name}-info.patch
URL:		http://www.xemacs.org/
BuildArch:	noarch
Requires:	xemacs
Requires:	xemacs-w3-pkg
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	xemacs-sumo

%description
Emacs/W3 provides some core functionality that can be readily re-used
from any program in Emacs. Users and other package writers are
encouraged to @i{Web-enable} their applications and daily work
routines with the library.

Emacs/W3 is completely customizable, both from Emacs-Lisp and from
stylesheets @xref{Stylesheets}. If there is any aspect of Emacs/W3
that cannot be modified to your satisfaction, please send mail to the
@t{w3-beta@@xemacs.org} mailing list with any suggestions.

%prep
%setup -q -c
%patch0 -p1

%build
(cd man/w3; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

gzip -9nf lisp/w3/{README.VMS,README,INSTALL,ChangeLog}

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/w3/*.gz
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
