Name: hello_world
Version: 1.0
Release: 1%{?dist}
Summary: A simple Hello, World! Python script

License: MIT
URL: https://github.com/Jeka4el/HelloWorld-CI
Source0: %{_sourcedir}/hello_world.py
BuildArch: noarch

%description
A simple Python script that prints "Hello, World!".

%prep
#%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 hello_world.py %{buildroot}%{_bindir}/hello_world

%files
%{_bindir}/hello_world
