Summary: Evolution addressbook search applet
Name: contact-lookup-applet
Version: 0.17
Release: %mkrel 1
License: GPLv2+
Group: Databases
URL: http://www.burtonini.com/
Source0: http://www.burtonini.com/computing/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: evolution-data-server-devel >= 0.0.95
BuildRequires: libglade2.0-devel
BuildRequires: libpanel-applet-devel
BuildRequires: automake1.9
BuildRequires: intltool

%description
This applet allows you to search your Evolution 2 address book for people. To
use, simply add it to your panel (Add to Panel -> Accessories -> Address book
Lookup), type a name into the field, and hit [return] or Search.

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog
%{_libdir}/bonobo/servers/*
%{_libdir}/contact-lookup-applet
%{_datadir}/lookup-applet


