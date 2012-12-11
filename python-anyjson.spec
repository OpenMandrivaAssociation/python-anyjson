%define	module	anyjson

Summary:	Python wrapper for JSON implementations
Name:		python-%{module}
Version:	0.3.3
Release:	1
Source0:	http://pypi.python.org/packages/source/a/anyjson/anyjson-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://bitbucket.org/runeh/anyjson
BuildArch:	noarch
Suggests:	python-json
Suggests:	python-cjson
Suggests:	python-simplejson
BuildRequires:	python-devel
BuildRequires:	python-setuptools

%description
Anyjson loads whichever is the fastest JSON module installed and provides
a uniform API regardless of which JSON implementation is used.

Originally part of carrot (http://github.com/ask/carrot/)

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc README



%changelog
* Mon Mar 28 2011 Lev Givon <lev@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 648693
- Update to 0.3.1.

* Wed Dec 08 2010 Lev Givon <lev@mandriva.org> 0.3-1mdv2011.0
+ Revision: 616287
- Update to 0.3.

* Tue Nov 09 2010 Lev Givon <lev@mandriva.org> 0.2.5-1mdv2011.0
+ Revision: 595458
- Update to 0.2.5.

* Mon Nov 08 2010 Lev Givon <lev@mandriva.org> 0.2.0-1mdv2011.0
+ Revision: 595123
- import python-anyjson



