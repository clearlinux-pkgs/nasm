#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nasm
Version  : 2.13.02
Release  : 23
URL      : http://www.nasm.us/pub/nasm/releasebuilds/2.13.02/nasm-2.13.02.tar.xz
Source0  : http://www.nasm.us/pub/nasm/releasebuilds/2.13.02/nasm-2.13.02.tar.xz
Summary  : The Netwide Assembler, a portable x86 assembler with Intel-like syntax
Group    : Development/Tools
License  : BSD-2-Clause
Requires: nasm-bin
Requires: nasm-doc
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

%description bin
bin components for the nasm package.


%package doc
Summary: doc components for the nasm package.
Group: Documentation

%description doc
doc components for the nasm package.


%prep
%setup -q -n nasm-2.13.02

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512764532
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
export SOURCE_DATE_EPOCH=1512764532
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nasm
/usr/bin/ndisasm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
