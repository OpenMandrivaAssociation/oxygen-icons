%define major	5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Oxygen icon theme
Name:		oxygen-icons
Version:	5.41.0
Release:	1
Epoch:		2
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}%{major}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)

Provides:	kde5-icon-theme
BuildArch:	noarch
%rename	oxygen-icon-theme

%description
Oxygen icon theme. Compliant with FreeDesktop.org naming schema.

%files
%{_iconsdir}/oxygen/
# This is needed as hicolor is the fallback for icons
%{_kde5_iconsdir}/hicolor/*/apps/*
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.*

#-----------------------------------------------------------------------------

%prep
%setup -qn %{name}%{major}-%{version}

%build
%cmake_kde5
cd ../
%ninja -C build

%install
%ninja_install -C build

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.filter << EOF
^./usr/share/icons/oxygen/
EOF
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/oxygen/
fi
EOF
chmod 755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.script

# We copy some missing icons from oxygen to hicolor
for size in 16 32 48 64 128; do
    mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/office-address-book.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/krdc.png  %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/akonadi.png  %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/kaffeine.png  %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/semn.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/plasmagik.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/ktip.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/kthesaurus.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/ksniffer.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/korgac.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/knewsticker.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/klipper.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/kjournal.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde5_iconsdir}/oxygen/base/${size}x${size}/apps/kivio.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
done
