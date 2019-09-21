Name:           xclip
Version:        0.13
Release:        1
Summary:        A command line interface to the X11 clipboard
Group:          Text tools
URL:            https://github.com/astrand/xclip
License:        GPLv2+
Source0:        https://github.com/astrand/xclip/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)

%description
xclip is a command line interface to the X11 clipboard. It can also be
used for copying files, as an alternative to sftp/scp, thus avoiding
password prompts when X11 forwarding has already been setup.

%prep
%setup -q

%build
autoreconf -fi
%configure
%make

%install
%makeinstall_std

%files
%_bindir/%{name}*
%_mandir/man1/%{name}*.1.*
