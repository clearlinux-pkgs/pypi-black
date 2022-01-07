#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-black
Version  : 21.12b0
Release  : 37
URL      : https://files.pythonhosted.org/packages/f7/60/7a9775dc1b81a572eb26836c7e77c92bf454ada00693af4b2d2f2614971a/black-21.12b0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f7/60/7a9775dc1b81a572eb26836c7e77c92bf454ada00693af4b2d2f2614971a/black-21.12b0.tar.gz
Summary  : The uncompromising code formatter.
Group    : Development/Tools
License  : MIT Python-2.0
Requires: pypi-black-bin = %{version}-%{release}
Requires: pypi-black-license = %{version}-%{release}
Requires: pypi-black-python = %{version}-%{release}
Requires: pypi-black-python3 = %{version}-%{release}
Requires: typed_ast
BuildRequires : buildreq-distutils3
Provides: black
Provides: black-python
Provides: black-python3
BuildRequires : pypi(pluggy)
BuildRequires : py-python
BuildRequires : pypi(click)
BuildRequires : pypi(mypy_extensions)
BuildRequires : pypi(pathspec)
BuildRequires : pypi(platformdirs)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(tomli)
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : typed_ast
BuildRequires : pypi(virtualenv)
Patch1: 0001-drop-upper-version-reqs.patch

%description
A subset of lib2to3 taken from Python 3.7.0b2.
Commit hash: 9c17e3a1987004b8bcfbe423953aad84493a7984

%package bin
Summary: bin components for the pypi-black package.
Group: Binaries
Requires: pypi-black-license = %{version}-%{release}

%description bin
bin components for the pypi-black package.


%package license
Summary: license components for the pypi-black package.
Group: Default

%description license
license components for the pypi-black package.


%package python
Summary: python components for the pypi-black package.
Group: Default
Requires: pypi-black-python3 = %{version}-%{release}

%description python
python components for the pypi-black package.


%package python3
Summary: python3 components for the pypi-black package.
Group: Default
Requires: python3-core
Provides: pypi(black)
Requires: pypi(aiohttp)
Requires: pypi(aiohttp_cors)
Requires: pypi(click)
Requires: pypi(mypy_extensions)
Requires: pypi(pathspec)
Requires: pypi(platformdirs)
Requires: pypi(tomli)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-black package.


%prep
%setup -q -n black-21.12b0
cd %{_builddir}/black-21.12b0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641420706
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . tomli
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-black
cp %{_builddir}/black-21.12b0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-black/edd079e7a759fe1fcf1d089e28b9c7df2080b42c
cp %{_builddir}/black-21.12b0/docs/_static/license.svg %{buildroot}/usr/share/package-licenses/pypi-black/e71d25df55070a88d192a9ecf3a7ad755e44e8ee
cp %{_builddir}/black-21.12b0/src/blib2to3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-black/8482348f12824b36fba59883f9dd7fe03c1f86ca
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} tomli
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/black
/usr/bin/black-primer
/usr/bin/blackd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-black/8482348f12824b36fba59883f9dd7fe03c1f86ca
/usr/share/package-licenses/pypi-black/e71d25df55070a88d192a9ecf3a7ad755e44e8ee
/usr/share/package-licenses/pypi-black/edd079e7a759fe1fcf1d089e28b9c7df2080b42c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
