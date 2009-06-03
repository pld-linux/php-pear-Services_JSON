%include	/usr/lib/rpm/macros.php
%define		_class		Services_JSON
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - PHP implementaion of json_encode/decode
Summary(pl.UTF-8):	%{_pearname} - prosty koder i dekoder dla notacji JSON
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://download.pear.php.net/package/Services_JSON-%{version}.tgz
# Source0-md5:	573ff2468330f7570c738957bc297ff4
URL:		http://pear.php.net/package/Services_JSON
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON (JavaScript Object Notation, <http://json.org>) is a lightweight
data-interchange format. It is easy for humans to read and write. It
is easy for machines to parse and generate. It is based on a subset of
the JavaScript Programming Language, Standard ECMA-262 3rd Edition -
December 1999. This feature can also be found in Python. JSON is a
text format that is completely language independent but uses
conventions that are familiar to programmers of the C-family of
languages, including C, C++, C#, Java, JavaScript, Perl, TCL, and many
others. These properties make JSON an ideal data-interchange language.

This package provides a simple encoder and decoder for JSON notation.
It is intended for use with client-side Javascript applications that
make use of HTTPRequest to perform server communication functions -
data can be encoded into JSON notation for use in a client-side
JavaScript, or decoded from incoming Javascript requests. JSON format
is native to JavaScript, and can be directly eval()'ed with no further
parsing overhead.

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
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/JSON.php
