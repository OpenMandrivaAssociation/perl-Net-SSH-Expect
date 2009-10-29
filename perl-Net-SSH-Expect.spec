%define upstream_name    Net-SSH-Expect
%define upstream_version 1.09

Name:       perl-%{upstream_name}
%if %mdkversion > 200900
Version:    %perl_convert_version %{upstream_version}
%else
Version:    %{upstream_version}
%endif
Release:    %mkrel 1
Summary:    An ssh wrapper to execute remote commands
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Expect)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a wrapper to the _ssh_ executable that is available in your
system's _$PATH_. Use this module to execute commands on the remote SSH
server. It authenticates with the user and password you passed in the
constructor's attributes 'user' and 'password'.

Once an ssh connection was started using the 'connect()' method it will
remain open until you call the 'close()' method. This allows you execute as
many commands as you want with the 'exec()' method using only one
connection. This is a better approach over other ssh wrapper
implementations, i.e: Net::SCP, Net::SSH and Net::SCP::Expect, that start a
new ssh connection each time a remote command is issued or a file is
transfered.

It uses _Expect.pm_ module to interact with the SSH server. A
'get_expect()' method is provided so you can obtain the internal 'Expect'
object connected to the SSH server. Use this only if you have some special
need that you can't do with the 'exec()' method.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


