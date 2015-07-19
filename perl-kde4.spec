%define srcname perlkde
%define with_kdepimlibs4 0

Summary:	KDE4 bindings for perl language
Name:		perl-kde4
Version:	4.14.3
Release:	3
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{srcname}-%{version}.tar.xz
BuildRequires:	perl-qt4-devel >= 1:%{version}
BuildRequires:	smokekde-devel
BuildRequires:	gdbm-devel
%if %{with_kdepimlibs4}
BuildRequires:	kdepimlibs4-devel
%endif
BuildRequires:	pkgconfig(shared-desktop-ontologies)
Requires:	perl-qt4 >= %{epoch}:%{version}

%description
A KDE4 bindings for perl language.

%prep
%setup -q -n %{srcname}-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files
%{_kde_libdir}/kde4/kperlpluginfactory.so
%if %{with_kdepimlibs4}
%{perl_sitearch}/QImageBlitz.pm
%{perl_sitearch}/Phonon.pm
%{perl_sitearch}/Qsci.pm
%{perl_sitearch}/auto/Phonon
%{perl_sitearch}/auto/QImageBlitz
%{perl_sitearch}/auto/Qsci
%endif
%{perl_sitearch}/Akonadi.pm
%{perl_sitearch}/Attica.pm
%{perl_sitearch}/KDECore4.pm
%{perl_sitearch}/KDEUi4.pm
%{perl_sitearch}/KFile.pm
%{perl_sitearch}/KHTML.pm
%{perl_sitearch}/KIO4.pm
%{perl_sitearch}/KNewStuff2.pm
%{perl_sitearch}/KNewStuff3.pm
%{perl_sitearch}/KParts.pm
%{perl_sitearch}/KTextEditor.pm
%{perl_sitearch}/KUtils.pm
%{perl_sitearch}/Nepomuk.pm
%{perl_sitearch}/NepomukQuery.pm
%{perl_sitearch}/Okular.pm
%{perl_sitearch}/Plasma4.pm
%{perl_sitearch}/Solid.pm
%{perl_sitearch}/Soprano.pm
%{perl_sitearch}/SopranoClient.pm
%{perl_sitearch}/SopranoServer.pm
%{perl_sitearch}/auto/Akonadi
%{perl_sitearch}/auto/Attica
%{perl_sitearch}/auto/KDECore4
%{perl_sitearch}/auto/KDEUi4
%{perl_sitearch}/auto/KFile
%{perl_sitearch}/auto/KHTML
%{perl_sitearch}/auto/KIO4
%{perl_sitearch}/auto/KNewStuff2
%{perl_sitearch}/auto/KNewStuff3
%{perl_sitearch}/auto/KParts
%{perl_sitearch}/auto/KTextEditor
%{perl_sitearch}/auto/KUtils
%{perl_sitearch}/auto/Nepomuk
%{perl_sitearch}/auto/NepomukQuery
%{perl_sitearch}/auto/Okular
%{perl_sitearch}/auto/Plasma4
%{perl_sitearch}/auto/Solid
%{perl_sitearch}/auto/Soprano
%{perl_sitearch}/auto/SopranoClient
%{perl_sitearch}/auto/SopranoServer

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
- Add pkgconfig(shared-desktop-ontologies) to BuildRequires

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

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Sun Jul 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Sat Jun 09 2012 Crispin Boylan <crisb@mandriva.org> 1:4.8.4-1
+ Revision: 803767
- New release

* Fri May 04 2012 Crispin Boylan <crisb@mandriva.org> 1:4.8.3-1
+ Revision: 796328
- New release

* Thu Apr 19 2012 Crispin Boylan <crisb@mandriva.org> 1:4.8.2-1
+ Revision: 792065
- New release

* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:4.8.0-1
+ Revision: 773652
- new version
- build with kdepimlibs
- apply some cosmetics

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New version
    - New version
    - Import perl-kde4
    - Create folder

