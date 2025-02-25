%define pulseversion %{expand:%(rpm -q --qf '[%%{version}]' pulseaudio)}
%define pulsemajorminor %{expand:%(echo '%{pulseversion}' | cut -d+ -f1)}
%define moduleversion %{pulsemajorminor}.%{expand:%(echo '%{version}' | cut -d. -f3)}

Name:       pulseaudio-module-keepalive
Summary:    PulseAudio keepalive module
Version:    1.1.0
Release:    1
License:    LGPLv2+
URL:        https://github.com/sailfishos/pulseaudio-module-keepalive
Source0:    %{name}-%{version}.tar.bz2
Requires:   pulseaudio >= %{pulseversion}
BuildRequires:  libtool-ltdl-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(pulsecore) >= %{pulsemajorminor}
BuildRequires:  pkgconfig(dbus-1)

%description
PulseAudio keepalive module.

%prep
%autosetup -n %{name}-%{version}

%build
echo "%{moduleversion}" > .tarball-version
%meson
%meson_build

%install
%meson_install

%files
%{_libdir}/pulse-*/modules/module-keepalive.so
%license COPYING
