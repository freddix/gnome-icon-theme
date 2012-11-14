%define		symbolic	3.6.2

Summary:	Default icon theme for GNOME enviroment
Name:		gnome-icon-theme
Version:	3.6.2
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	c7bf0c7cc3ca0c9d4ac120aedb9ab8af
Source1:	http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme-symbolic/3.6/%{name}-symbolic-%{symbolic}.tar.xz
# Source1-md5:	5c6a3834d50a14ff3c6d65513ac36eb4
URL:		http://www.gnome.org/
BuildRequires:	gdk-pixbuf
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
%setup -q -a1

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

cd %{name}-symbolic-%{symbolic}
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

