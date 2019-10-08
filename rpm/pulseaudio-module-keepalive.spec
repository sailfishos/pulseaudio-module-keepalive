%define pulseversion %{expand:%(rpm -q --qf '[%%{version}]' pulseaudio)}
%define pulsemajorminor %{expand:%(echo '%{pulseversion}' | cut -d+ -f1)}
%define moduleversion %{pulsemajorminor}.%{expand:%(echo '%{version}' | cut -d. -f3)}

Name:       pulseaudio-module-keepalive
Summary:    PulseAudio keepalive module
Version:    1.0.0
Release:    1
Group:      Multimedia/PulseAudio
License:    LGPLv2+
URL:        https://git.sailfishos.org/mer-core/pulseaudio-module-keepalive
Source0:    %{name}-%{version}.tar.bz2
Requires:   pulseaudio >= %{pulseversion}
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pkgconfig(pulsecore) >= %{pulsemajorminor}
BuildRequires:  pkgconfig(dbus-1)

%description
PulseAudio keepalive module.

%prep
%setup -q -n %{name}-%{version}

%build
echo "%{moduleversion}" > .tarball-version
%reconfigure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_libdir}/pulse-%{pulsemajorminor}/modules/module-keepalive.so
%license COPYING
