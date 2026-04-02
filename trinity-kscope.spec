%bcond clang 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg kscope
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Version:	1.6.2
Release:	%{?tde_version:%{tde_version}_}3
Summary:	Source editing environment for TDE
Group:		Applications/Internet
URL:		http://kscope.sourceforge.net

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/development/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}


BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext
Requires:		cscope

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

BuildRequires:	flex
BuildRequires:	bison

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
KScope is a TDE front-end to Cscope. It provides a source-editing environment
for large C projects. KScope is focused on source editing and analysis.

KScope is built around an efficient mechanism for code-navigation, which
allows the user to run queries on the code.

The types of queries KScope can run include:
* Get all references to a symbol
* Find the definition of a symbol
* Find all functions called by or calling to a function
* Find an EGrep pattern
* Find all files #including some file

These queries are handled by an underlying Cscope process. KScope simply
serves as a front-end to this process, feeding it with queries, and parsing
its output into result lists. The items in those lists can later be selected
to open an editor at the matching line.

Main Features:
* Multiple editor windows (using your favourite TDE editor)
* Project management
* Front-end to most Cscope queries
* Tag list for every open editor
* Call-tree window
* Session management, including saving and restoring queries
* Works with externally-built cscope.out files


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md ChangeLog
%{tde_prefix}/bin/kscope
%{tde_prefix}/share/applications/tde/kscope.desktop
%{tde_prefix}/share/apps/kscope/
%{tde_prefix}/share/doc/tde/HTML/en/kscope/
%{tde_prefix}/share/icons/hicolor/*/apps/kscope.png
%{tde_prefix}/share/icons/locolor/*/apps/kscope.png
%{tde_prefix}/share/man/man1/kscope.1*

