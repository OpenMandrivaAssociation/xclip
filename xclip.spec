Name:           xclip
Version:        0.12
Release:        %mkrel 3
Summary:        A command line interface to the X11 clipboard
Group:          Text tools
URL:            http://sourceforge.net/projects/xclip
License:        GPLv2+
Source0:        http://sourceforge.net/projects/xclip/files/xclip/0.12/%{name}-%{version}.tar.gz
BuildRequires:  libx11-devel
BuildRequires:	libxmu-devel
BuildRoot:      %_tmppath/%{name}-%{version}-%{release}

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
