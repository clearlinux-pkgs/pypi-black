#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v3
# autospec commit: c1050fe
#
Name     : pypi-black
Version  : 23.12.1
Release  : 72
URL      : https://files.pythonhosted.org/packages/fd/f4/a57cde4b60da0e249073009f4a9087e9e0a955deae78d3c2a493208d0c5c/black-23.12.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/fd/f4/a57cde4b60da0e249073009f4a9087e9e0a955deae78d3c2a493208d0c5c/black-23.12.1.tar.gz
Summary  : The uncompromising code formatter.
Group    : Development/Tools
License  : MIT Python-2.0
Requires: pypi-black-bin = %{version}-%{release}
Requires: pypi-black-license = %{version}-%{release}
Requires: pypi-black-python = %{version}-%{release}
Requires: pypi-black-python3 = %{version}-%{release}
Requires: pypi(typed_ast)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_fancy_pypi_readme)
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
BuildRequires : pypi(py)
BuildRequires : pypi(typed_ast)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
A subset of lib2to3 taken from Python 3.7.0b2. Commit hash:
9c17e3a1987004b8bcfbe423953aad84493a7984

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
Requires: pypi(packaging)
Requires: pypi(pathspec)
Requires: pypi(platformdirs)
Requires: pypi(tomli)

%description python3
python3 components for the pypi-black package.


%prep
%setup -q -n black-23.12.1
cd %{_builddir}/black-23.12.1
pushd ..
cp -a black-23.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703607441
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . tomli
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . tomli
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-black
cp %{_builddir}/black-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-black/edd079e7a759fe1fcf1d089e28b9c7df2080b42c || :
cp %{_builddir}/black-%{version}/docs/_static/license.svg %{buildroot}/usr/share/package-licenses/pypi-black/e71d25df55070a88d192a9ecf3a7ad755e44e8ee || :
cp %{_builddir}/black-%{version}/src/blib2to3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-black/8482348f12824b36fba59883f9dd7fe03c1f86ca || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} tomli
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/black
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
