%define libxprintapputil %mklibname xprintapputil 1
Name: libxprintapputil
Summary:  The XprintAppUtil Library
Version: 1.0.1
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXprintAppUtil-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root


BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxp-devel >= 1.0.0
BuildRequires: libxprintutil-devel >= 1.0.1
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description 
The XprintAppUtil Library

#-----------------------------------------------------------

%package -n %{libxprintapputil}
Summary:  The XprintAppUtil Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxprintapputil}
The XprintAppUtil Library

#-----------------------------------------------------------

%package -n %{libxprintapputil}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxprintapputil} = %{version}
Requires: x11-proto-devel >= 1.0.0
Requires: libx11-devel >= 1.0.0
Requires: libxprintutil-devel >= 1.0.1
Provides: libxprintapputil-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxprintapputil}-devel
Development files for %{name}

%pre -n %{libxprintapputil}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxprintapputil}-devel
%defattr(-,root,root)
%{_libdir}/libXprintAppUtil.so
%{_libdir}/libXprintAppUtil.la
%{_libdir}/pkgconfig/xprintapputil.pc
%{_includedir}/X11/XprintAppUtil/xpapputil.h

#-----------------------------------------------------------

%package -n %{libxprintapputil}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxprintapputil}-devel = %{version}
Provides: libxprintapputil-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxprintapputil}-static-devel
Static development files for %{name}

%files -n %{libxprintapputil}-static-devel
%defattr(-,root,root)
%{_libdir}/libXprintAppUtil.a

#-----------------------------------------------------------

%prep
%setup -q -n libXprintAppUtil-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxprintapputil}
%defattr(-,root,root)
%{_libdir}/libXprintAppUtil.so.1
%{_libdir}/libXprintAppUtil.so.1.0.0

