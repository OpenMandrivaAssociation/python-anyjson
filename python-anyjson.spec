%define module  anyjson

Summary:    Python wrapper for JSON implementations
Name:       python-%{module}
Version:    0.3.3
Release:    4
Source0:    http://pypi.python.org/packages/source/a/anyjson/anyjson-%{version}.tar.gz
License:    BSD
Group:      Development/Python
Url:        http://bitbucket.org/runeh/anyjson
Suggests:   python-json
Suggests:   python-cjson
Suggests:   python-simplejson
BuildRequires:  python-devel
BuildRequires:  python3-devel
BuildRequires:	python-distribute
BuildRequires:	python3-distribute
BuildArch: noarch

%description
Anyjson loads whichever is the fastest JSON module installed and provides
a uniform API regardless of which JSON implementation is used.

Originally part of carrot (http://github.com/ask/carrot/)

%package -n python3-anyjson
Summary:        Python wrapper for JSON implementations
Group:          Development/Python
Requires:       python3
 
%description -n python3-anyjson
Anyjson loads whichever is the fastest JSON module installed and provides
a uniform API regardless of which JSON implementation is used.

Originally part of carrot (http://github.com/ask/carrot/)

%prep
%setup -q -c

mv %{module}-%{version} python2
cp -r python2 python3

%build
pushd python2
%{__python} setup.py build
popd

pushd python3
%{__python3} setup.py build
popd

%install
pushd python2
%{__python} setup.py install --root=%{buildroot} 
popd

pushd python3
%{__python3} setup.py install --root=%{buildroot}
popd

%files -n python-anyjson
%doc python2/README 
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/%{module}

%files -n python3-anyjson
%doc python3/README
%{py3_puresitedir}/*.egg-info
%{py3_puresitedir}/%{module}
