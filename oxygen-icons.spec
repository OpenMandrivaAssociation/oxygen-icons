Summary:	Oxygen icon theme
Name:		oxygen-icons
Version:	14.12.1
Release:	1
Epoch:		1
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	kde4-macros
Provides:	kde4-icon-theme
BuildArch:	noarch

%description
Oxygen icon theme. Compliant with FreeDesktop.org naming schema

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
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.filter << EOF
^./usr/share/icons/oxygen/
EOF
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/oxygen
fi
EOF
chmod 755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.script

# We copy some missing icons from oxygen to hicolor
for size in 16 32 48 64 128; do
    mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/office-address-book.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/krdc.png  %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/akonadi.png  %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/kaffeine.png  %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/semn.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/plasmagik.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/ktip.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/kthesaurus.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/ksniffer.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/korgac.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/knewsticker.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/klipper.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/kjournal.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp %{buildroot}%{_kde_iconsdir}/oxygen/${size}x${size}/apps/kivio.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
done

%post
%update_icon_cache oxygen

%postun
%clean_icon_cache oxygen

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0
- Dont copy kexi icon

* Sun Jan 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.5-1
- New version 4.9.5

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Thu Jul 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Thu Jul 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762424
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758113
- New version

* Sun Jan 01 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 748654
- New version

* Wed Dec 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 740824
- New version

* Thu Dec 08 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 739031
- New upstream tarball 4.7.80

* Fri Aug 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 697228
- New version 4.7.41
- New version 4.7.41

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-1
+ Revision: 684418
- New version 4.6.4

* Thu May 12 2011 Funda Wang <fwang@mandriva.org> 1:4.6.3-1
+ Revision: 673710
- new version 4.6.3

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.2-1
+ Revision: 650785
- Remove mkrel
- New version 4.6.2

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.1-5
+ Revision: 640743
- New version 4.6.1

* Thu Feb 17 2011 Funda Wang <fwang@mandriva.org> 1:4.6.0-5
+ Revision: 638228
- really disable rpm5's trigger

* Thu Feb 17 2011 Funda Wang <fwang@mandriva.org> 1:4.6.0-4
+ Revision: 638186
- revert to old style file trigger

* Sun Feb 13 2011 Funda Wang <fwang@mandriva.org> 1:4.6.0-3
+ Revision: 637528
- rebuild for fixed rpm-setup-mandriva

* Sun Feb 13 2011 Funda Wang <fwang@mandriva.org> 1:4.6.0-2
+ Revision: 637504
- convert file trigger into rpm5 file trigger

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.0-1
+ Revision: 632979
- New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.95-1mdv2011.0
+ Revision: 629144
- New version KDE 4.6 RC2

* Fri Dec 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.90-1mdv2011.0
+ Revision: 624553
- Commit good tarball
- Remove wrong tarball
- New upstream tarball

* Wed Dec 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.85-1mdv2011.0
+ Revision: 616361
- New upstream tarball

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 1:4.5.80-1mdv2011.0
+ Revision: 601422
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 1:4.5.77-1mdv2011.0
+ Revision: 599089
- new snapshot 4.5.77

* Thu Oct 28 2010 Funda Wang <fwang@mandriva.org> 1:4.5.74-1mdv2011.0
+ Revision: 589663
- new snapshot 4.5.74

* Tue Sep 14 2010 Funda Wang <fwang@mandriva.org> 1:4.5.68-1mdv2011.0
+ Revision: 578134
- new snapshot 4.5.68

* Mon Sep 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.67-1mdv2011.0
+ Revision: 576402
- New version 4.5.67

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.0-1mdv2011.0
+ Revision: 566584
- New upstream tarball
- Update to version 4.5.0

* Wed Jul 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.95-1mdv2011.0
+ Revision: 562633
- kde 4.4.95

* Mon Jun 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-2mdv2010.1
+ Revision: 549334
- Some more icons addition
- Add missing hicolor icons

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-1mdv2010.1
+ Revision: 542142
- Update to version 4.4.3

* Sun Apr 18 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-2mdv2010.1
+ Revision: 536120
- Karbon hicolor icons are available in karbon package now

* Wed Mar 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-1mdv2010.1
+ Revision: 530079
- Fix install step
- Fix version
- Update to version 4.4.2

* Tue Mar 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-1mdv2010.1
+ Revision: 513425
- Update to version 4.4.1

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-1mdv2010.1
+ Revision: 502638
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-1mdv2010.1
+ Revision: 499106
- Fix version
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.95-4mdv2010.1
+ Revision: 496134
- Update to kde 4.4 Rc2

* Tue Jan 19 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-4mdv2010.1
+ Revision: 493747
- kcolorchooser does not belong to here

* Tue Jan 19 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-3mdv2010.1
+ Revision: 493699
- Bump release
- Remove kig icons, this is not necessary to have them here

* Tue Jan 19 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-2mdv2010.1
+ Revision: 493552
- Add more missing icons on hicolor
- Akonadi icon is needed on hicolor too
- Copy krdc on hicolor too
- Add icons on hicolor to be ok with the specs

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-1mdv2010.1
+ Revision: 488225
- Update to kde 4.4 rc1

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.85-1mdv2010.1
+ Revision: 480704
- Update to kde 4.4 beta2

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.80-2mdv2010.1
+ Revision: 473376
- Fix typo

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.80-1mdv2010.1
+ Revision: 473186
- Update to kde 4.4 Beta1
- Fix typo in description

* Sat Nov 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.77-1mdv2010.1
+ Revision: 470733
- Remove debug
- Update to kde 4.3.77
- Update to kde 4.3.77

* Mon Nov 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.75-1mdv2010.1
+ Revision: 466561
- Update to kde 4.3.75

* Sun Nov 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-1mdv2010.1
+ Revision: 462882
- Update to kde 4.3.73

* Tue Oct 06 2009 Funda Wang <fwang@mandriva.org> 1:4.3.2-2mdv2010.0
+ Revision: 454450
- add conflicts

* Mon Oct 05 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.2-1mdv2010.0
+ Revision: 454116
- New upstream release 4.3.2.

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-1mdv2010.0
+ Revision: 423137
- New upstream release 4.3.1.

* Thu Aug 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.0-2mdv2010.0
+ Revision: 410946
- Add conflics to ease upgrade

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.0-1mdv2010.0
+ Revision: 408790
- New upstream release 4.3.0.

* Wed Jul 22 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.98-1mdv2010.0
+ Revision: 398671
- KDE 4.3 RC3

* Sat Jul 11 2009 Funda Wang <fwang@mandriva.org> 1:4.2.96-1mdv2010.0
+ Revision: 394441
- new version 4.2.96

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-1mdv2010.0
+ Revision: 389229
- Update to kde 4.3Rc1

* Fri Jun 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.90-1mdv2010.0
+ Revision: 383155
- Update to beta2

* Fri May 29 2009 Funda Wang <fwang@mandriva.org> 1:4.2.88-1mdv2010.0
+ Revision: 380762
- New version 4.2.88

* Fri May 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.87-1mdv2010.0
+ Revision: 378634
- Update to kde   4.2.87

* Sun May 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-4mdv2010.0
+ Revision: 373916
- Fix conflicts

* Sat May 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-3mdv2010.0
+ Revision: 373715
- Add conflicts

* Fri May 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-2mdv2010.0
+ Revision: 373473
- Fix conflicts with kdepim

* Fri May 08 2009 Funda Wang <fwang@mandriva.org> 1:4.2.85-1mdv2010.0
+ Revision: 373116
- New version 4.2.85

* Mon May 04 2009 Funda Wang <fwang@mandriva.org> 1:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371531
- New version 4.2.71
- should be noarch package
- there is no need to build it, just installing is enough

* Thu Apr 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 369155
- Update to kde 4.2.70

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.2-2mdv2009.1
+ Revision: 361678
- Raise epoch to match old package

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 4.2.2-1mdv2009.1
+ Revision: 361602
- Oxygen icons now are a independent package
- import oxygen-icon-theme


