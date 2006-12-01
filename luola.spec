Summary:	Multiplayer Cave-flying game
Summary(pl):	Sieciowa gra zrêczno¶ciowa
Name:		luola
Version:	1.3.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.luolamies.org/software/luola/%{name}-%{version}.tar.gz
# Source0-md5:	029f48e8fb8d104e9634cf20c4493460
Source1:	http://www.luolamies.org/software/luola/stdlevels-6.0.tar.gz
# Source1-md5:	7660b90d67c06726c1849c3ff0e24aea
Source2:	http://www.luolamies.org/software/luola/nostalgia-1.2.tar.gz
# Source2-md5:	4777681fa97ada351ebaf954ba8451ef
Patch0:		%{name}-desktop.patch
URL:		http://www.luolamies.org/software/luola/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Luola is a cavern-flying game for 2-4 players. Each player flies a
small V-shaped ship and has one special weapon. The object of the game
is simply to destroy all other players.

%description -l pl
Luola to zrêczno¶ciówka dla 2-4 graczy. Ka¿dy gracz lata ma³ym
statkiem w kszta³cie litery V po ró¿nych poziomach. Celem gry jest
zniszczenie wszystkich pozosta³ych graczy.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install luola.desktop $RPM_BUILD_ROOT%{_desktopdir}
install luola.png $RPM_BUILD_ROOT%{_pixmapsdir}
tar xvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/%{name}/levels
tar xvf %{SOURCE2} -C $RPM_BUILD_ROOT%{_datadir}/%{name}/levels

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS RELEASENOTES.txt README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
