%define name autosmb
%define version 1.1
%define release 7

Summary: Automounter script for autods
Name: %name
Version: %version
Release: %release
License: GPL
Group: System/Kernel and hardware
URL: https://www.historischtheater.be/ddemerre/
Source1: auto.smb
Source2: auto.smb.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: samba-client, autofs
BuildArch: noarch

%description
This is an automounter helper script for autofs.

Add this to /etc/auto.master 

	/cifs   /etc/auto.smb   --timeout=60

and edit /etc/auto.smb.conf with credentials. The credemntials
file should be of the form

username=NTDOMAIN\USERNAME
password=PASSWORD

%prep 

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -m 500 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install -m 500 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/auto.smb
%config(noreplace) /etc/auto.smb.conf
%doc



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-6mdv2011.0
+ Revision: 616656
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.1-5mdv2010.0
+ Revision: 423993
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.1-4mdv2009.0
+ Revision: 226202
- rebuild
- fix spacing at top of description

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2008.1
+ Revision: 122276
- kill re-definition of %%buildroot on Pixel's request
- import autosmb


* Thu Oct 20 2005 Lenny Cartier <lenny@mandriva.com> 1.1-3mdk
- rebuild

* Thu Jan 29 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1-2mdk
- from Robin Rosenberg <robin.rosenberg@dewire.com> :
	- Initial build.
