%include	/usr/lib/rpm/macros.php
%define		_class		JSON
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - Simple encoder and decoder for JSON notation
Summary(pl):	%{_pearname} - prosty koder i dekoder dla notacji JSON
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	0.1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://mike.teczno.com/JSON.tar.gz
# Source0-md5:	fc2cec5a87fe3d70ecbe0857f30eac94
URL:		http://pear.php.net/pepr/pepr-proposal-show.php?id=198
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a simple encoder and decoder for JSON notation.
It is intended for use with client-side Javascript applications that
make use of HTTPRequest to perform server communication functions -
data can be encoded into JSON notation for use in a client-side
Javascript, or decoded from incoming Javascript requests. JSON format
is native to Javascript, and can be directly eval()'ed with no further
parsing overhead.

%description -l pl
Ten pakiet udostêpnia prosty koder i dekoder dla notacji JSON. Jest
przeznaczony do u¿ywania z aplikacjami w Javascripcie po stronie
klienta korzystaj±cymi z HTTPRequest do komunikacji z serwerem - dane
mog± byæ kodowane w notacji JSON do u¿ywania z poziomu Javascriptu po
stronie klienta lub dekodowane z przychodz±cych ¿±dañ Javascriptu.
Format JSON jest natywny dla Javascriptu i mo¿e byæ bezpo¶rednio
wykonany przez eval() bez dalszego przetwarzania.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/tests
install JSON.php $RPM_BUILD_ROOT%{php_pear_dir}
install Test-JSON.php $RPM_BUILD_ROOT%{php_pear_dir}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{php_pear_dir}/JSON.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
