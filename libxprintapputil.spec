%define major 1
%define libname %mklibname xprintapputil %{major}
%define devname %mklibname -d xprintapputil

Summary:	The XprintAppUtil library
Name:		libxprintapputil
Version:	1.0.1
Release:	13
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXprintAppUtil-%{version}.tar.bz2
BuildRequires:	x11-proto-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xp)
BuildRequires:	pkgconfig(xprintutil)

%description
The XprintAppUtil library.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	The XprintAppUtil library
Group:		Development/X11

%description -n %{libname}
The XprintAppUtil Library.

%files -n %{libname}
%{_libdir}/libXprintAppUtil.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{_lib}xprintapputil-static-devel < 1.0.1-13

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_libdir}/libXprintAppUtil.so
%{_libdir}/pkgconfig/xprintapputil.pc
%{_includedir}/X11/XprintAppUtil/xpapputil.h

#----------------------------------------------------------------------------

%prep
%setup -q -n libXprintAppUtil-%{version}

%build
%configure2_5x\
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

