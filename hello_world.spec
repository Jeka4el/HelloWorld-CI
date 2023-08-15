Name: hello_world
Version: 1.0
Release: 1%{?dist}
Summary: A simple Hello, World! Python script
License: MIT
URL: https://github.com/Jeka4el/HelloWorld-CI

# Используем абсолютные пути к файлам
Source0: /home/runner/rpmbuild/SOURCES/hello_world.py
Source1: /home/runner/rpmbuild/SPECS/hello_world.spec

BuildArch: noarch

%description
A simple Python script that prints "Hello, World!".

%prep
#%setup -q

%build

%install
#rm -rf /
mkdir -p /usr/bin
echo "Installing /home/runner/rpmbuild/SOURCES/hello_world.py to /usr/bin/hello_world"
install -p -m 755 /home/runner/rpmbuild/SOURCES/hello_world.py /usr/bin/hello_world
echo "Installing /home/runner/rpmbuild/SPECS/hello_world.spec to /usr/share/hello_world/hello_world.spec"
install -p -m 644 /home/runner/rpmbuild/SPECS/hello_world.spec /usr/share/hello_world/hello_world.spec


%files
%{_bindir}/hello_world
%{_specdir}/hello_world.spec
