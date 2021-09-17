Name:           zaproxy
Version:        2.10.0
Release:        1%{?dist}
Summary:        The OWASP Zed Attack Proxy

# For a breakdown of the licensing, see LEGALNOTICE.md
License:        ASL 2.0
URL:            https://www.zaproxy.org
Source0:        https://github.com/zaproxy/zaproxy/archive/v%{version}.tar.gz
Source1:        %{name}.desktop
BuildArch:      noarch

BuildRequires:  java-11-openjdk
BuildRequires:  desktop-file-utils

Requires:       java

%description
The OWASP Zed Attack Proxy (ZAP) is one of the world’s most popular free
security tools and is actively maintained by a dedicated international team
of volunteers. It can help you automatically find security vulnerabilities in
your web applications while you are developing and testing your applications.
Its also a great tool for experienced pentesters to use for manual security
testing.

%prep
%autosetup

%build
JAVA_HOME=/usr/lib/jvm/jre-11-openjdk ./gradlew build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -r zap/build/distFiles/. %{buildroot}%{_datadir}/%{name}/

for r in 16 32 48 64 128 256 512; do
	install -m 644 -D zap/build/resources/main/resource/zap${r}x${r}.png \
	 %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/%{name}.png
done

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%files
%license LICENSE LEGALNOTICE.md
%doc README.md
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Sep 17 2021 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.10.0-1
- Update to 2.10.0

* Sat Feb 22 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.9.0-1
- Initial build
