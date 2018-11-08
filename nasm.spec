#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nasm
Version  : 2.14
Release  : 29
URL      : http://www.nasm.us/pub/nasm/releasebuilds/2.14/nasm-2.14.tar.xz
Source0  : http://www.nasm.us/pub/nasm/releasebuilds/2.14/nasm-2.14.tar.xz
Summary  : The Netwide Assembler, a portable x86 assembler with Intel-like syntax
Group    : Development/Tools
License  : BSD-2-Clause
Requires: nasm-bin = %{version}-%{release}
Requires: nasm-license = %{version}-%{release}
Requires: nasm-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : groff
BuildRequires : xmlto

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%package bin
Summary: bin components for the nasm package.
Group: Binaries
Requires: nasm-license = %{version}-%{release}
Requires: nasm-man = %{version}-%{release}

%description bin
bin components for the nasm package.


%package license
Summary: license components for the nasm package.
Group: Default

%description license
license components for the nasm package.


%package man
Summary: man components for the nasm package.
Group: Default

%description man
man components for the nasm package.


%prep
%setup -q -n nasm-2.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541641929
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
export SOURCE_DATE_EPOCH=1541641929
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nasm
cp LICENSE %{buildroot}/usr/share/package-licenses/nasm/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nasm
/usr/bin/ndisasm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nasm/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/nasm.1
/usr/share/man/man1/ndisasm.1
