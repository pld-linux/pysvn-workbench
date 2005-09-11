%bcond_with	tests

%define	module	WorkBench
Summary:	Python SVN GUI Tools
Name:		python-workbench
Version:	1.1.6
Release:	1
License:	Apache Group License
Group:		Development/Languages/Python
Source0:	http://pysvn.tigris.org/files/documents/1233/22212/WorkBench-%{version}.tar.gz
# Source0-md5:	47e69a287d78e0bb2e9f7f401e8b78e0
URL:		http://pysvn.tigris.org/
BuildRequires:	python-devel
%pyrequires_eq	python
Requires:	python-pysvn
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

%prep
%setup  -q -n WorkBench-%{version}

%build

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
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/*
