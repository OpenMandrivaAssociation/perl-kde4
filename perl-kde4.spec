%define srcname perlkde
%define with_kdepimlibs4 0

Name:		perl-kde4
Summary:	KDE4 bindings for perl language
Version: 4.9.0
Release: 1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{srcname}-%{version}.tar.xz
BuildRequires:	perl-qt4-devel >= 1:%{version}
BuildRequires:	smokekde-devel
BuildRequires:	gdbm-devel
%if %{with_kdepimlibs4}
BuildRequires:	kdepimlibs4-devel
%endif
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
%{perl_sitearch}/Kate.pm
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
%{perl_sitearch}/auto/Kate
%{perl_sitearch}/auto/Nepomuk
%{perl_sitearch}/auto/NepomukQuery
%{perl_sitearch}/auto/Okular
%{perl_sitearch}/auto/Plasma4
%{perl_sitearch}/auto/Solid
%{perl_sitearch}/auto/Soprano
%{perl_sitearch}/auto/SopranoClient
%{perl_sitearch}/auto/SopranoServer

