#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-File-ShareDir-Dist
Version  : 1.001002
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Test-File-ShareDir-1.001002.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Test-File-ShareDir-1.001002.tar.gz
Summary  : 'Create a Fake ShareDir for your modules for testing.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Class::Tiny)
BuildRequires : perl(File::Copy::Recursive)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Scope::Guard)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)

%description
Test::File::ShareDir
"Test::File::ShareDir" is some low level plumbing to enable a
distribution to perform tests while consuming its own "share"
directories in a manner similar to how they will be once installed.

%package dev
Summary: dev components for the perl-Test-File-ShareDir-Dist package.
Group: Development
Provides: perl-Test-File-ShareDir-Dist-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-File-ShareDir-Dist package.


%prep
%setup -q -n Test-File-ShareDir-1.001002

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Test/File/ShareDir.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/File/ShareDir/Dist.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/File/ShareDir/Module.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/File/ShareDir/Object/Dist.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/File/ShareDir/Object/Inc.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/File/ShareDir/Object/Module.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/File/ShareDir/TempDirObject.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/File/ShareDir/Utils.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::File::ShareDir.3
/usr/share/man/man3/Test::File::ShareDir::Dist.3
/usr/share/man/man3/Test::File::ShareDir::Module.3
/usr/share/man/man3/Test::File::ShareDir::Object::Dist.3
/usr/share/man/man3/Test::File::ShareDir::Object::Inc.3
/usr/share/man/man3/Test::File::ShareDir::Object::Module.3
/usr/share/man/man3/Test::File::ShareDir::TempDirObject.3
/usr/share/man/man3/Test::File::ShareDir::Utils.3
