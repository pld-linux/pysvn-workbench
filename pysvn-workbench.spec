%bcond_with	tests

%define	module	WorkBench
Summary:	Python SVN GUI Tools
Summary(pl.UTF-8):	Graficzne narzędzia w Pythonie do SVN
Name:		python-workbench
Version:	1.5.3
Release:	1
License:	Apache Group License
Group:		Development/Languages/Python
Source0:	http://pysvn.barrys-emacs.org/source_kits/WorkBench-%{version}.tar.gz
# Source0-md5:	52c93ebbe89e8ffd7c203c50fab258ea
URL:		http://pysvn.tigris.org/
BuildRequires:	python-devel
%pyrequires_eq	python
Requires:	python-pysvn
Requires:	python-wxPython
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

cp -a Source/* $RPM_BUILD_ROOT%{_datadir}/%{name}
sed -i -e 's#wb_main.py#%{_datadir}/%{name}/wb_main.py#g' $RPM_BUILD_ROOT%{_datadir}/%{name}/wb.sh
ln -s %{_datadir}/%{name}/wb.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/toolbar_images
%{_datadir}/%{name}/*.py*
%{_datadir}/%{name}/pylintrc
%{_datadir}/%{name}/wb.ic*
%{_datadir}/%{name}/wb.png
%{_datadir}/%{name}/wb.tiff
%attr(755,root,root) %{_datadir}/%{name}/*.sh
