%define name autosmb
%define version 1.1
%define release %mkrel 6

Summary: Automounter script for autods
Name: %name
Version: %version
Release: %release
License: GPL
Group: System/Kernel and hardware
URL: http://www.historischtheater.be/ddemerre/
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

