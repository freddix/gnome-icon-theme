%define		symbolic	3.12.0
%define		extras		3.12.0

Summary:	Default icon theme for GNOME enviroment
Name:		gnome-icon-theme
Version:	3.12.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	f14bed7f804e843189ffa7021141addd
Source1:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme-extras/3.12/%{name}-extras-%{extras}.tar.xz
# Source1-md5:	91f8f7e35a3d8d926716d88b8b1e9a29
Source2:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme-symbolic/3.12/%{name}-symbolic-%{symbolic}.tar.xz
# Source2-md5:	3c9c0e6b9fa04b3cbbb84da825a26fd9
URL:		http://www.gnome.org/
BuildRequires:	/usr/bin/gtk-update-icon-cache
BuildRequires:	icon-naming-utils
BuildRequires:	intltool
BuildArch:	noarch
Provides:	xdg-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkgconfigdir	%{_datadir}/pkgconfig

%description
Default icon theme for GNOME enviroment.

%package devel
Summary:	Pkgconfig file
Group:		Development

%description devel
GNOME icon theme pkgconfig file.

%prep
%setup -q -a1 -a2

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

cd %{name}-extras-%{extras}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

cd ../%{name}-symbolic-%{symbolic}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__make} -C %{name}-extras-%{extras} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__make} -C %{name}-symbolic-%{symbolic} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%{_iconsdir}/gnome

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc

