Name:		oxygen-icon-theme
Summary:	Oxygen icon theme
Group:		Graphical desktop/KDE
Version: 4.9.3
Release: 1
Epoch:		1
License:	GPL
Provides:	kde4-icon-theme
URL:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/oxygen-icons-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	kde4-macros
BuildArch:	noarch

%description
Oxygen KDE 4 icon theme. Compliant with FreeDesktop.org naming schema

%files
%{_iconsdir}/oxygen
# This is needed as hicolor is the fallback for icons
%{_kde_iconsdir}/hicolor/*/apps/*
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.*

#-----------------------------------------------------------------------------

%prep
%setup -q -n oxygen-icons-%{version}

%build
%cmake_kde4

%install
%makeinstall_std -C build

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
%__install -d %{buildroot}%{_var}/lib/rpm/filetriggers
%__cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.filter << EOF
^./usr/share/icons/oxygen/
EOF
%__cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/oxygen
fi
EOF
%__chmod 755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.script

# We copy some missing icons from oxygen to hicolor
for size in 16 32 48 64 128; do
    %__mkdir_p %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/office-address-book.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/krdc.png  %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/akonadi.png  %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/kaffeine.png  %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/semn.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/plasmagik.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/ktip.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/kthesaurus.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/ksniffer.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/korgac.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/knewsticker.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/klipper.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/kjournal.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/kivio.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    %__cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/kexi.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
done

%post
%update_icon_cache oxygen

%postun
%clean_icon_cache oxygen

