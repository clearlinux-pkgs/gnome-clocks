#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-clocks
Version  : 43.0
Release  : 15
URL      : https://download.gnome.org/sources/gnome-clocks/43/gnome-clocks-43.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-clocks/43/gnome-clocks-43.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-clocks-bin = %{version}-%{release}
Requires: gnome-clocks-data = %{version}-%{release}
Requires: gnome-clocks-license = %{version}-%{release}
Requires: gnome-clocks-locales = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : geoclue-dev
BuildRequires : gsound-dev
BuildRequires : pkgconfig(gnome-desktop-4)
BuildRequires : pkgconfig(gsound)
BuildRequires : pkgconfig(gweather4)
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(libgeoclue-2.0)

%description
# GNOME Clocks
A simple clock application for GNOME. It includes world clocks, alarms,
a stopwatch and a timer.

%package bin
Summary: bin components for the gnome-clocks package.
Group: Binaries
Requires: gnome-clocks-data = %{version}-%{release}
Requires: gnome-clocks-license = %{version}-%{release}

%description bin
bin components for the gnome-clocks package.


%package data
Summary: data components for the gnome-clocks package.
Group: Data

%description data
data components for the gnome-clocks package.


%package doc
Summary: doc components for the gnome-clocks package.
Group: Documentation

%description doc
doc components for the gnome-clocks package.


%package license
Summary: license components for the gnome-clocks package.
Group: Default

%description license
license components for the gnome-clocks package.


%package locales
Summary: locales components for the gnome-clocks package.
Group: Default

%description locales
locales components for the gnome-clocks package.


%prep
%setup -q -n gnome-clocks-43.0
cd %{_builddir}/gnome-clocks-43.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663950846
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-clocks
cp %{_builddir}/gnome-clocks-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/gnome-clocks/13d2034b5ee3cb8d1a076370cf8f0e344a5d0855 || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-clocks

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-clocks

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.clocks.desktop
/usr/share/dbus-1/services/org.gnome.clocks.service
/usr/share/glib-2.0/schemas/org.gnome.clocks.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.clocks.search-provider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.clocks.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.clocks-symbolic.svg
/usr/share/metainfo/org.gnome.clocks.metainfo.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-clocks/alarm-add.page
/usr/share/help/C/gnome-clocks/alarm-edit.page
/usr/share/help/C/gnome-clocks/alarm-remove.page
/usr/share/help/C/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/C/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/C/gnome-clocks/index.page
/usr/share/help/C/gnome-clocks/legal.xml
/usr/share/help/C/gnome-clocks/stopwatch.page
/usr/share/help/C/gnome-clocks/timer.page
/usr/share/help/C/gnome-clocks/world-add.page
/usr/share/help/C/gnome-clocks/world-check.page
/usr/share/help/C/gnome-clocks/world-remove.page
/usr/share/help/ca/gnome-clocks/alarm-add.page
/usr/share/help/ca/gnome-clocks/alarm-edit.page
/usr/share/help/ca/gnome-clocks/alarm-remove.page
/usr/share/help/ca/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/ca/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/ca/gnome-clocks/index.page
/usr/share/help/ca/gnome-clocks/legal.xml
/usr/share/help/ca/gnome-clocks/stopwatch.page
/usr/share/help/ca/gnome-clocks/timer.page
/usr/share/help/ca/gnome-clocks/world-add.page
/usr/share/help/ca/gnome-clocks/world-check.page
/usr/share/help/ca/gnome-clocks/world-remove.page
/usr/share/help/cs/gnome-clocks/alarm-add.page
/usr/share/help/cs/gnome-clocks/alarm-edit.page
/usr/share/help/cs/gnome-clocks/alarm-remove.page
/usr/share/help/cs/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/cs/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/cs/gnome-clocks/index.page
/usr/share/help/cs/gnome-clocks/legal.xml
/usr/share/help/cs/gnome-clocks/stopwatch.page
/usr/share/help/cs/gnome-clocks/timer.page
/usr/share/help/cs/gnome-clocks/world-add.page
/usr/share/help/cs/gnome-clocks/world-check.page
/usr/share/help/cs/gnome-clocks/world-remove.page
/usr/share/help/da/gnome-clocks/alarm-add.page
/usr/share/help/da/gnome-clocks/alarm-edit.page
/usr/share/help/da/gnome-clocks/alarm-remove.page
/usr/share/help/da/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/da/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/da/gnome-clocks/index.page
/usr/share/help/da/gnome-clocks/legal.xml
/usr/share/help/da/gnome-clocks/stopwatch.page
/usr/share/help/da/gnome-clocks/timer.page
/usr/share/help/da/gnome-clocks/world-add.page
/usr/share/help/da/gnome-clocks/world-check.page
/usr/share/help/da/gnome-clocks/world-remove.page
/usr/share/help/de/gnome-clocks/alarm-add.page
/usr/share/help/de/gnome-clocks/alarm-edit.page
/usr/share/help/de/gnome-clocks/alarm-remove.page
/usr/share/help/de/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/de/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/de/gnome-clocks/index.page
/usr/share/help/de/gnome-clocks/legal.xml
/usr/share/help/de/gnome-clocks/stopwatch.page
/usr/share/help/de/gnome-clocks/timer.page
/usr/share/help/de/gnome-clocks/world-add.page
/usr/share/help/de/gnome-clocks/world-check.page
/usr/share/help/de/gnome-clocks/world-remove.page
/usr/share/help/el/gnome-clocks/alarm-add.page
/usr/share/help/el/gnome-clocks/alarm-edit.page
/usr/share/help/el/gnome-clocks/alarm-remove.page
/usr/share/help/el/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/el/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/el/gnome-clocks/index.page
/usr/share/help/el/gnome-clocks/legal.xml
/usr/share/help/el/gnome-clocks/stopwatch.page
/usr/share/help/el/gnome-clocks/timer.page
/usr/share/help/el/gnome-clocks/world-add.page
/usr/share/help/el/gnome-clocks/world-check.page
/usr/share/help/el/gnome-clocks/world-remove.page
/usr/share/help/en_GB/gnome-clocks/alarm-add.page
/usr/share/help/en_GB/gnome-clocks/alarm-edit.page
/usr/share/help/en_GB/gnome-clocks/alarm-remove.page
/usr/share/help/en_GB/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/en_GB/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/en_GB/gnome-clocks/index.page
/usr/share/help/en_GB/gnome-clocks/legal.xml
/usr/share/help/en_GB/gnome-clocks/stopwatch.page
/usr/share/help/en_GB/gnome-clocks/timer.page
/usr/share/help/en_GB/gnome-clocks/world-add.page
/usr/share/help/en_GB/gnome-clocks/world-check.page
/usr/share/help/en_GB/gnome-clocks/world-remove.page
/usr/share/help/es/gnome-clocks/alarm-add.page
/usr/share/help/es/gnome-clocks/alarm-edit.page
/usr/share/help/es/gnome-clocks/alarm-remove.page
/usr/share/help/es/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/es/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/es/gnome-clocks/index.page
/usr/share/help/es/gnome-clocks/legal.xml
/usr/share/help/es/gnome-clocks/stopwatch.page
/usr/share/help/es/gnome-clocks/timer.page
/usr/share/help/es/gnome-clocks/world-add.page
/usr/share/help/es/gnome-clocks/world-check.page
/usr/share/help/es/gnome-clocks/world-remove.page
/usr/share/help/eu/gnome-clocks/alarm-add.page
/usr/share/help/eu/gnome-clocks/alarm-edit.page
/usr/share/help/eu/gnome-clocks/alarm-remove.page
/usr/share/help/eu/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/eu/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/eu/gnome-clocks/index.page
/usr/share/help/eu/gnome-clocks/legal.xml
/usr/share/help/eu/gnome-clocks/stopwatch.page
/usr/share/help/eu/gnome-clocks/timer.page
/usr/share/help/eu/gnome-clocks/world-add.page
/usr/share/help/eu/gnome-clocks/world-check.page
/usr/share/help/eu/gnome-clocks/world-remove.page
/usr/share/help/fi/gnome-clocks/alarm-add.page
/usr/share/help/fi/gnome-clocks/alarm-edit.page
/usr/share/help/fi/gnome-clocks/alarm-remove.page
/usr/share/help/fi/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/fi/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/fi/gnome-clocks/index.page
/usr/share/help/fi/gnome-clocks/legal.xml
/usr/share/help/fi/gnome-clocks/stopwatch.page
/usr/share/help/fi/gnome-clocks/timer.page
/usr/share/help/fi/gnome-clocks/world-add.page
/usr/share/help/fi/gnome-clocks/world-check.page
/usr/share/help/fi/gnome-clocks/world-remove.page
/usr/share/help/fr/gnome-clocks/alarm-add.page
/usr/share/help/fr/gnome-clocks/alarm-edit.page
/usr/share/help/fr/gnome-clocks/alarm-remove.page
/usr/share/help/fr/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/fr/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/fr/gnome-clocks/index.page
/usr/share/help/fr/gnome-clocks/legal.xml
/usr/share/help/fr/gnome-clocks/stopwatch.page
/usr/share/help/fr/gnome-clocks/timer.page
/usr/share/help/fr/gnome-clocks/world-add.page
/usr/share/help/fr/gnome-clocks/world-check.page
/usr/share/help/fr/gnome-clocks/world-remove.page
/usr/share/help/gl/gnome-clocks/alarm-add.page
/usr/share/help/gl/gnome-clocks/alarm-edit.page
/usr/share/help/gl/gnome-clocks/alarm-remove.page
/usr/share/help/gl/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/gl/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/gl/gnome-clocks/index.page
/usr/share/help/gl/gnome-clocks/legal.xml
/usr/share/help/gl/gnome-clocks/stopwatch.page
/usr/share/help/gl/gnome-clocks/timer.page
/usr/share/help/gl/gnome-clocks/world-add.page
/usr/share/help/gl/gnome-clocks/world-check.page
/usr/share/help/gl/gnome-clocks/world-remove.page
/usr/share/help/hu/gnome-clocks/alarm-add.page
/usr/share/help/hu/gnome-clocks/alarm-edit.page
/usr/share/help/hu/gnome-clocks/alarm-remove.page
/usr/share/help/hu/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/hu/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/hu/gnome-clocks/index.page
/usr/share/help/hu/gnome-clocks/legal.xml
/usr/share/help/hu/gnome-clocks/stopwatch.page
/usr/share/help/hu/gnome-clocks/timer.page
/usr/share/help/hu/gnome-clocks/world-add.page
/usr/share/help/hu/gnome-clocks/world-check.page
/usr/share/help/hu/gnome-clocks/world-remove.page
/usr/share/help/id/gnome-clocks/alarm-add.page
/usr/share/help/id/gnome-clocks/alarm-edit.page
/usr/share/help/id/gnome-clocks/alarm-remove.page
/usr/share/help/id/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/id/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/id/gnome-clocks/index.page
/usr/share/help/id/gnome-clocks/legal.xml
/usr/share/help/id/gnome-clocks/stopwatch.page
/usr/share/help/id/gnome-clocks/timer.page
/usr/share/help/id/gnome-clocks/world-add.page
/usr/share/help/id/gnome-clocks/world-check.page
/usr/share/help/id/gnome-clocks/world-remove.page
/usr/share/help/it/gnome-clocks/alarm-add.page
/usr/share/help/it/gnome-clocks/alarm-edit.page
/usr/share/help/it/gnome-clocks/alarm-remove.page
/usr/share/help/it/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/it/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/it/gnome-clocks/index.page
/usr/share/help/it/gnome-clocks/legal.xml
/usr/share/help/it/gnome-clocks/stopwatch.page
/usr/share/help/it/gnome-clocks/timer.page
/usr/share/help/it/gnome-clocks/world-add.page
/usr/share/help/it/gnome-clocks/world-check.page
/usr/share/help/it/gnome-clocks/world-remove.page
/usr/share/help/ko/gnome-clocks/alarm-add.page
/usr/share/help/ko/gnome-clocks/alarm-edit.page
/usr/share/help/ko/gnome-clocks/alarm-remove.page
/usr/share/help/ko/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/ko/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/ko/gnome-clocks/index.page
/usr/share/help/ko/gnome-clocks/legal.xml
/usr/share/help/ko/gnome-clocks/stopwatch.page
/usr/share/help/ko/gnome-clocks/timer.page
/usr/share/help/ko/gnome-clocks/world-add.page
/usr/share/help/ko/gnome-clocks/world-check.page
/usr/share/help/ko/gnome-clocks/world-remove.page
/usr/share/help/nl/gnome-clocks/alarm-add.page
/usr/share/help/nl/gnome-clocks/alarm-edit.page
/usr/share/help/nl/gnome-clocks/alarm-remove.page
/usr/share/help/nl/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/nl/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/nl/gnome-clocks/index.page
/usr/share/help/nl/gnome-clocks/legal.xml
/usr/share/help/nl/gnome-clocks/stopwatch.page
/usr/share/help/nl/gnome-clocks/timer.page
/usr/share/help/nl/gnome-clocks/world-add.page
/usr/share/help/nl/gnome-clocks/world-check.page
/usr/share/help/nl/gnome-clocks/world-remove.page
/usr/share/help/pl/gnome-clocks/alarm-add.page
/usr/share/help/pl/gnome-clocks/alarm-edit.page
/usr/share/help/pl/gnome-clocks/alarm-remove.page
/usr/share/help/pl/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/pl/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/pl/gnome-clocks/index.page
/usr/share/help/pl/gnome-clocks/legal.xml
/usr/share/help/pl/gnome-clocks/stopwatch.page
/usr/share/help/pl/gnome-clocks/timer.page
/usr/share/help/pl/gnome-clocks/world-add.page
/usr/share/help/pl/gnome-clocks/world-check.page
/usr/share/help/pl/gnome-clocks/world-remove.page
/usr/share/help/pt_BR/gnome-clocks/alarm-add.page
/usr/share/help/pt_BR/gnome-clocks/alarm-edit.page
/usr/share/help/pt_BR/gnome-clocks/alarm-remove.page
/usr/share/help/pt_BR/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/pt_BR/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/pt_BR/gnome-clocks/index.page
/usr/share/help/pt_BR/gnome-clocks/legal.xml
/usr/share/help/pt_BR/gnome-clocks/stopwatch.page
/usr/share/help/pt_BR/gnome-clocks/timer.page
/usr/share/help/pt_BR/gnome-clocks/world-add.page
/usr/share/help/pt_BR/gnome-clocks/world-check.page
/usr/share/help/pt_BR/gnome-clocks/world-remove.page
/usr/share/help/ru/gnome-clocks/alarm-add.page
/usr/share/help/ru/gnome-clocks/alarm-edit.page
/usr/share/help/ru/gnome-clocks/alarm-remove.page
/usr/share/help/ru/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/ru/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/ru/gnome-clocks/index.page
/usr/share/help/ru/gnome-clocks/legal.xml
/usr/share/help/ru/gnome-clocks/stopwatch.page
/usr/share/help/ru/gnome-clocks/timer.page
/usr/share/help/ru/gnome-clocks/world-add.page
/usr/share/help/ru/gnome-clocks/world-check.page
/usr/share/help/ru/gnome-clocks/world-remove.page
/usr/share/help/sv/gnome-clocks/alarm-add.page
/usr/share/help/sv/gnome-clocks/alarm-edit.page
/usr/share/help/sv/gnome-clocks/alarm-remove.page
/usr/share/help/sv/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/sv/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/sv/gnome-clocks/index.page
/usr/share/help/sv/gnome-clocks/legal.xml
/usr/share/help/sv/gnome-clocks/stopwatch.page
/usr/share/help/sv/gnome-clocks/timer.page
/usr/share/help/sv/gnome-clocks/world-add.page
/usr/share/help/sv/gnome-clocks/world-check.page
/usr/share/help/sv/gnome-clocks/world-remove.page
/usr/share/help/tr/gnome-clocks/alarm-add.page
/usr/share/help/tr/gnome-clocks/alarm-edit.page
/usr/share/help/tr/gnome-clocks/alarm-remove.page
/usr/share/help/tr/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/tr/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/tr/gnome-clocks/index.page
/usr/share/help/tr/gnome-clocks/legal.xml
/usr/share/help/tr/gnome-clocks/stopwatch.page
/usr/share/help/tr/gnome-clocks/timer.page
/usr/share/help/tr/gnome-clocks/world-add.page
/usr/share/help/tr/gnome-clocks/world-check.page
/usr/share/help/tr/gnome-clocks/world-remove.page
/usr/share/help/uk/gnome-clocks/alarm-add.page
/usr/share/help/uk/gnome-clocks/alarm-edit.page
/usr/share/help/uk/gnome-clocks/alarm-remove.page
/usr/share/help/uk/gnome-clocks/alarm-snooze-stop.page
/usr/share/help/uk/gnome-clocks/figures/gnome-clocks.png
/usr/share/help/uk/gnome-clocks/index.page
/usr/share/help/uk/gnome-clocks/legal.xml
/usr/share/help/uk/gnome-clocks/stopwatch.page
/usr/share/help/uk/gnome-clocks/timer.page
/usr/share/help/uk/gnome-clocks/world-add.page
/usr/share/help/uk/gnome-clocks/world-check.page
/usr/share/help/uk/gnome-clocks/world-remove.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-clocks/13d2034b5ee3cb8d1a076370cf8f0e344a5d0855

%files locales -f gnome-clocks.lang
%defattr(-,root,root,-)

