%define		symbolic	3.8.2.2
%define		extras		3.6.2

Summary:	Default icon theme for GNOME enviroment
Name:		gnome-icon-theme
Version:	3.8.2
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	d645c5a504daa64730dfc083344de1b9
Source1:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme-extras/3.6/%{name}-extras-%{extras}.tar.xz
# Source1-md5:	41a37beccf627237d98eef2b472e9c4d
Source2:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme-symbolic/3.8/%{name}-symbolic-%{symbolic}.tar.xz
# Source2-md5:	34fbeb90af63a5b7e492a04435253876
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

