#
# Conditional build:
%bcond_with	tests		# build with tests

Summary:	Python SVN GUI Tools
Summary(pl.UTF-8):	Graficzne narzędzia w Pythonie do SVN
Name:		pysvn-workbench
Version:	1.7.0
Release:	0.3
License:	Apache
Group:		Development/Languages/Python
Source0:	http://pysvn.barrys-emacs.org/source_kits/WorkBench-%{version}.tar.gz
# Source0-md5:	aed0cc35a87c6dd287ad6a1a2fcf5b06
URL:		http://pysvn.tigris.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	desktop-file-utils
Requires:	python
Requires:	python-pysvn >= 1.8.0
Requires:	python-wxPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pysvn WorkBench Features:
- Easy to learn and use
- All subversion client operations in a GUI
- Support software development workflow
- Builtin GUI diff showing line and character diffs
- Ability to diff between revisions in a files history
- Runs on Windows and Unix platforms
- Implemented in Python, allowing customisation

%description -l pl.UTF-8
Cechy pysvn WorkBench:
- łatwy do nauki i używania
- wszystkie operacje klienckie subversion z poziomu GUI
- obsługa przepływu pracy przy tworzeniu oprogramowania
- wbudowany graficzny diff pokazujący różnice linii i znaków
- możliwość porównywania między rewizjami plików w historii
- działa na platformach Windows i Unix
- zaimplementowany w Pythonie, konfigurowalny

%prep
%setup -q -n WorkBench-%{version}

ln -s Source/linux-rpmbuild.mak Makefile

%{__sed} -i -e 's/install /install -p /' Makefile

%build
%{__make} \
	PYTHON=%{__python}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pysvn-workbench
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py*
%{_desktopdir}/pysvn-workbench.desktop
%{_datadir}/%{name}/wb.png
