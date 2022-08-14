#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-black
Version  : 22.6.0
Release  : 48
URL      : https://files.pythonhosted.org/packages/61/11/551b0d067a7e6836fc0997ab36ee46ec65259fea8f30104f4870092f3301/black-22.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/61/11/551b0d067a7e6836fc0997ab36ee46ec65259fea8f30104f4870092f3301/black-22.6.0.tar.gz
Summary  : The uncompromising code formatter.
Group    : Development/Tools
License  : MIT Python-2.0
Requires: pypi-black-bin = %{version}-%{release}
Requires: pypi-black-license = %{version}-%{release}
Requires: pypi-black-python = %{version}-%{release}
Requires: pypi-black-python3 = %{version}-%{release}
Requires: pypi(typed_ast)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)
BuildRequires : pypi(mypy_extensions)
BuildRequires : pypi(pathspec)
BuildRequires : pypi(platformdirs)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(typed_ast)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

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

%description python3
python3 components for the pypi-black package.


%prep
%setup -q -n black-22.6.0
cd %{_builddir}/black-22.6.0
pushd ..
cp -a black-22.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656441616
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
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . tomli
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-black
cp %{_builddir}/black-22.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-black/edd079e7a759fe1fcf1d089e28b9c7df2080b42c
cp %{_builddir}/black-22.6.0/docs/_static/license.svg %{buildroot}/usr/share/package-licenses/pypi-black/e71d25df55070a88d192a9ecf3a7ad755e44e8ee
cp %{_builddir}/black-22.6.0/src/blib2to3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-black/8482348f12824b36fba59883f9dd7fe03c1f86ca
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} tomli
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
