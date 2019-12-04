Name:           dbus-c++
Version:        0.9.0
Release:        20
Summary:        Native C++ bindings for D-Bus
License:        LGPLv2+
URL:            http://sourceforge.net/projects/dbus-cplusplus/
Source0:        http://downloads.sourceforge.net/dbus-cplusplus/libdbus-c++-%{version}.tar.gz

Patch0001:      dbus-c++-gcc4.7.patch
Patch0002:      dbus-c++-linkfix.patch
Patch0003:      dbus-c++-macro_collision.patch
Patch0004:      dbus-c++-threading.patch
Patch0005:      dbus-c++-writechar.patch

BuildRequires:  gcc-c++ dbus-devel glib2-devel gtkmm24-devel autoconf automake libtool expat-devel ecore-devel
Provides:       %{name}-ecore = %{version}-%{release} %{name}-glib = %{version}-%{release}
Obsoletes:      %{name}-ecore < %{version}-%{release} %{name}-glib < %{version}-%{release}

%description
dbus-c++ attempts to provide a C++ API for D-BUS. The library has a glib/gtk and an Ecore mainloop
integration.It also offers an optional own main loop.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release} pkgconfig

%description devel
This package contains libraries and header files for developing applications that use %{name}.

%prep
%autosetup -n libdbus-c++-%{version} -p1
sed -i 's/libtoolize --force --copy/libtoolize -if --copy/' bootstrap

%build
autoreconf -vfi
export CPPFLAGS='-pthread %{optflags}' CXXFLAGS='--std=gnu++11 -pthread %{optflags}'
%configure --disable-static
%make_build

%install
%make_install
%delete_la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING
%{_bindir}/dbusxx-*
%{_libdir}/libdbus-c++-*1.so.0*

%files devel
%doc TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Mon Dec  2 2019 lingsheng <lingsheng@huawei.com> - 0.9.0-20
- Package init
