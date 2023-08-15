Name: hello_world
Version: 1.0
Release: 1%{?dist}
Summary: A simple Hello, World! Python script
License: MIT
URL: https://github.com/Jeka4el/HelloWorld-CI

# Используйте относительные пути к файлам
Source0: /home/runner/rpmbuild/SOURCES/hello_world.py
Source1: /home/runner/rpmbuild/SPECS/hello_world.spec

BuildArch: noarch

%description
A simple Python script that prints "Hello, World!".

%prep
#%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 /home/runner/rpmbuild/SOURCES/hello_world.py %{buildroot}%{_bindir}/hello_world
install -p -m 644 /home/runner/rpmbuild/SPECS/hello_world.spec %{buildroot}%{_specdir}/hello_world.spec

%files
%{_bindir}/hello_world
%{_specdir}/hello_world.spec
