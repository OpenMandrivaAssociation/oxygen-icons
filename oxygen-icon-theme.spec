Name: oxygen-icon-theme
Summary: Oxygen icon theme
Group: Graphical desktop/KDE
Version: 4.3.2
Release: %mkrel 1
Epoch: 1
License: GPL
Provides: kde4-icon-theme
Obsoletes: kdelibs4-common >= 30000000:3.80.3
URL: http://www.kde.org
Source0: ftp://ftp.kde.org/pub/kde/unstable/%version/src/oxygen-icons-%version.tar.bz2
BuildRequires: cmake
BuildRequires: kde4-macros
BuildArch: noarch
Conflicts: kdebase4-workspace < 2:4.1.96-1
Conflicts: kappfinder < 1:4.1.96-2
Conflicts: kdepim4-core < 2:4.2.85-2
Conflicts: kdeedu4-core < 4.3.0-3
BuildRoot: %_tmppath/%name-%version-%release-root

%description
Oxygen KDE 4 icon theme. Complains with FreeDesktop.org naming schema

%files
%defattr(-,root,root,-)
%_iconsdir/oxygen
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.*

#-----------------------------------------------------------------------------

%prep
%setup -q -n oxygen-icons-%version

%build
%cmake_kde4

%install
rm -rf %buildroot

%makeinstall_std -C build

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %buildroot%{_var}/lib/rpm/filetriggers
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.filter << EOF
^./usr/share/icons/oxygen/
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/oxygen
fi
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.script

%clean
rm -fr %buildroot
