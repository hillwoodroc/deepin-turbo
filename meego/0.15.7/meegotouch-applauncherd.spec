# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.21
# 
# >> macros
# << macros

Name:       meegotouch-applauncherd
Summary:    Application launcher for fast startup
Version:    0.15.7
Release:    1
Group:      System/Daemons
License:    LGPLv2+
URL:        http://meego.gitorious.com/meegotouch/meegotouch-applauncherd
Source0:    %{name}-%{version}.tar.bz2
Source100:  meegotouch-applauncherd.yaml
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(meegotouch)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xext)
BuildRequires:  cmake


%description
Application invoker and launcher daemon that speed up
application startup time.



%package devel
Summary:    Development files for launchable applications
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for creating applications that can be launched 
using meegotouch-applauncherd.


%package testapps
Summary:    Test applications for launchable applications
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description testapps
Test applications used for testing meegotouch-applauncherd.


%package tests
Summary:    Test scripts for launchable applications
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-testapps = %{version}-%{release}
BuildRequires:   desktop-file-utils

%description tests
Test scripts used for testing meegotouch-applauncherd.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
export BUILD_TESTS=1
export MEEGO=1
unset LD_AS_NEEDED
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# rpmlint complains about installing binaries in /usr/share, so
# move them elsewhere and leave a symlink in place.
mv %{buildroot}/usr/share/applauncherd-tests %{buildroot}/usr/lib
(cd %{buildroot}/usr/share; ln -s ../lib/applauncherd-tests)
# << install post















%files
%defattr(-,root,root,-)
%{_bindir}/invoker
%{_libdir}/applauncherd/libapplauncherd.so
%{_bindir}/applauncherd.bin
%{_bindir}/applauncherd
%config %{_sysconfdir}/xdg/autostart/applauncherd.desktop
# >> files
# << files


%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/meegotouch-boostable.pc
%{_libdir}/pkgconfig/qt-boostable.pc
%doc %{_docdir}/applauncherd/README
%{_datadir}/qt4/mkspecs/features/meegotouch-boostable.prf
%{_datadir}/qt4/mkspecs/features/qt-boostable.prf
# >> files devel
# << files devel

%files testapps
%defattr(-,root,root,-)
%{_bindir}/fala_ft_hello
%{_bindir}/fala_gettime_ms
%{_bindir}/fala_pixelchanged
%{_bindir}/fala_wl
%{_bindir}/fala_wl.launch
%{_bindir}/fala_wol
%{_bindir}/fala_wol.sh
%{_bindir}/fala_gettime
%{_bindir}/fala_status.launch
%{_bindir}/fala_ft_hello1
%{_bindir}/fala_ft_hello2
%{_bindir}/fala_ft_hello.launch
%{_bindir}/fala_ft_hello1.launch
%{_bindir}/fala_ft_hello2.launch
%{_bindir}/fala_testapp
%{_bindir}/fala_ft_themetest.launch
%{_bindir}/fala_ft_themetest
%{_bindir}/fala_windowid
%{_datadir}/themes/base/meegotouch/fala_ft_themetest/svg/baa.svg
%{_datadir}/dbus-1/services/com.nokia.fala_testapp.service
# >> files testapps
# << files testapps

%files tests
%defattr(-,root,root,-)
%{_datadir}/applauncherd-M-art-tests/tests.xml
%{_datadir}/applauncherd-M-bug-tests/tests.xml
%{_datadir}/applauncherd-M-functional-tests/tests.xml
%{_datadir}/applauncherd-M-performance-tests/tests.xml
%{_datadir}/applauncherd-tests
%{_libdir}/applauncherd-tests/tests.xml
%{_libdir}/applauncherd-tests/ut_booster
%{_libdir}/applauncherd-tests/ut_connection
%{_libdir}/applauncherd-tests/ut_daemon
%{_libdir}/applauncherd-tests/ut_mbooster
%{_libdir}/applauncherd-tests/ut_qtbooster
%{_libdir}/applauncherd-tests/ut_boosterfactory
%{_libdir}/applauncherd-tests/ut_wrtbooster
%{_datadir}/applauncherd-M-testscripts/check_pipes.py
%exclude %{_datadir}/applauncherd-M-testscripts/check_pipes.pyc
%exclude %{_datadir}/applauncherd-M-testscripts/check_pipes.pyo
%{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_m.py
%exclude %{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_m.pyc
%exclude %{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_m.pyo
%{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_m.sh
%{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_qt.py
%exclude %{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_qt.pyc
%exclude %{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_qt.pyo
%{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_qt.sh
%{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_wrt.py
%exclude %{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_wrt.pyc
%exclude %{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_wrt.pyo
%{_datadir}/applauncherd-M-testscripts/signal-forward/fala_sf_wrt.sh
%{_datadir}/applauncherd-M-testscripts/tc_theming.rb
%{_datadir}/applauncherd-M-testscripts/test-func-launcher.py
%exclude %{_datadir}/applauncherd-M-testscripts/test-func-launcher.pyc
%exclude %{_datadir}/applauncherd-M-testscripts/test-func-launcher.pyo
%{_datadir}/applauncherd-M-testscripts/test-perf-mbooster.py
%exclude %{_datadir}/applauncherd-M-testscripts/test-perf-mbooster.pyc
%exclude %{_datadir}/applauncherd-M-testscripts/test-perf-mbooster.pyo
%{_datadir}/applauncherd-M-testscripts/ts_prestartapp.rb
%{_datadir}/applauncherd-M-testscripts/fala_wid
%{_datadir}/applauncherd-M-testscripts/fala_xres_wl
%{_datadir}/applauncherd-M-testscripts/fala_xres_wol
%{_datadir}/applauncherd-M-testscripts/test-perf.rb
%{_datadir}/applauncherd-M-testscripts/utils.py
%exclude %{_datadir}/applauncherd-M-testscripts/utils.pyc
%exclude %{_datadir}/applauncherd-M-testscripts/utils.pyo
%{_datadir}/themes/base/meegotouch/fala_ft_themetest/style/fala_ft_themetest.css
%{_datadir}/applications/fala_wl.desktop
%{_datadir}/applications/fala_wol.desktop
%{_datadir}/dbus-1/services/com.nokia.fala_wl.service
%{_datadir}/dbus-1/services/com.nokia.fala_wol.service
# >> files tests
# << files tests

