#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Alien
%define		pnam	Libxml2
Summary:	Alien::Libxml2 - provide the C libxml2 library
Summary(pl.UTF-8):	Alien::Libxml2 - dostarczenie biblioteki C libxml2
Name:		perl-Alien-Libxml2
Version:	0.16
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	746d7452f1bbdd2707f07319ae4a5444
URL:		https://metacpan.org/release/Alien-Libxml2
BuildRequires:	libxml2-devel >= 1:2.9.5
BuildRequires:	perl-Alien-Base
BuildRequires:	perl-Alien-Build >= 2.12
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.52
BuildRequires:	perl-Test-Alien
BuildRequires:	perl-Test2-Suite >= 0.000060
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
This module provides libxml2 for other modules to use.

%description -l pl.UTF-8
Ten pakiet udostępnia bibliotekę libxml2 do użycia przez inne moduły.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Alien/Libxml2.pm
%{perl_vendorarch}/Alien/Libxml2
%dir %{perl_vendorarch}/auto/Alien/Libxml2
%{perl_vendorarch}/auto/Alien/Libxml2/Libxml2.txt
%{perl_vendorarch}/auto/share/dist/Alien-Libxml2
%{_mandir}/man3/Alien::Libxml2.3pm*
