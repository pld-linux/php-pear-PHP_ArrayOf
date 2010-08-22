%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	ArrayOf
%define		_status		alpha
%define		_pearname	PHP_ArrayOf
Summary:	%{_pearname} - Abstract class package to create arrays of specific element types
Summary(pl.UTF-8):	%{_pearname} - abstrakcyjna klasa do tworzenia tablic z elementów określonego typu
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d2b2145c2cfe1a78ad629bc8f3d150b6
URL:		http://pear.php.net/package/PHP_ArrayOf/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows to create classes similar to ArrayObject with additional
element type or index constraints.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten pozwala na tworzenie klas zbliżonych do ArrayObject z
dodatkowymi ograniczeniami dotyczącymi typu elementu lub indeksu.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/PHP_ArrayOf/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PHP/ArrayOf
%{php_pear_dir}/PHP/ArrayOf.php
%{php_pear_dir}/PHP/ArrayOfInterface.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/PHP_ArrayOf
