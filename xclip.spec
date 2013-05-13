Name:           xclip
Version:        0.12
Release:        4
Summary:        A command line interface to the X11 clipboard
Group:          Text tools
URL:            http://sourceforge.net/projects/xclip
License:        GPLv2+
Source0:        http://sourceforge.net/projects/xclip/files/xclip/0.12/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)

%description
xclip is a command line interface to the X11 clipboard. It can also be
used for copying files, as an alternative to sftp/scp, thus avoiding
password prompts when X11 forwarding has already been setup.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%_bindir/%{name}*
%_mandir/man1/%{name}*.1.*


%changelog
* Thu Feb 10 2011 Funda Wang <fwang@mandriva.org> 0.12-3mdv2011.0
+ Revision: 637140
- tighten BR

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.12-2mdv2011.0
+ Revision: 615509
- the mass rebuild of 2010.1 packages

* Sun Apr 25 2010 Rémy Clouard <shikamaru@mandriva.org> 0.12-1mdv2010.1
+ Revision: 538530
- clean spec
- import xclip


