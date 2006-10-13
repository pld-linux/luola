Summary:	Multiplayer Cave-flying game
Summary(pl):	Sieciowa gra zr�czno�ciowa
Name:		luola
Version:	1.3.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.luolamies.org/software/luola/%{name}-%{version}.tar.gz
# Source0-md5:	029f48e8fb8d104e9634cf20c4493460
Source1:	http://www.luolamies.org/software/luola/stdlevels-6.0.tar.gz
# Source1-md5:	7660b90d67c06726c1849c3ff0e24aea
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
Luola to zr�czno�ci�wka dla 2-4 graczy. Ka�dy gracz lata ma�ym
statkiem w kszta�cie litery V po r�nych poziomach. Celem gry jest
zniszczenie wszystkich pozosta�ych graczy.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

tar xvvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/%{name}/levels

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS RELEASENOTES.txt README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}