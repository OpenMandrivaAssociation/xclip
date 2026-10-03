Name:		xclip
Version:	0.13
Release:	1
Summary:	A command line interface to the X11 clipboard
Group:		Text tools
URL:		https://github.com/astrand/xclip
License:	GPL-2.0-or-later
Source0:	https://github.com/astrand/xclip/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnu-config
BuildRequires:	make
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)

%description
xclip is a command line interface to the X11 clipboard. It can also be
used for copying files, as an alternative to sftp/scp, thus avoiding
password prompts when X11 forwarding has already been setup.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README ChangeLog
%{_bindir}/xclip*
%{_mandir}/man1/xclip*.1*
