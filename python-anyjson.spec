%define	module	anyjson
%define name	python-%{module}
%define version	0.3.3
%define release 1

Summary:	Python wrapper for JSON implementations
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/a/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://bitbucket.org/runeh/anyjson
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Suggests:	python-json, python-cjson, python-simplejson
BuildRequires:	python-devel, python-setuptools

%description
Anyjson loads whichever is the fastest JSON module installed and provides
a uniform API regardless of which JSON implementation is used.

Originally part of carrot (http://github.com/ask/carrot/)

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} 

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%py_sitedir/anyjson*

