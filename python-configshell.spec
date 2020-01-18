# Copyright 2011, Red Hat

%global oname configshell-fb

Name:           python-configshell
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        A framework to implement simple but nice CLIs
Epoch:          1
Version:        1.1.fb23
Release:        4%{?dist}
URL:            https://fedorahosted.org/targetcli-fb/
Source:         https://fedorahosted.org/released/targetcli-fb/%{oname}-%{version}.tar.gz
Patch0:         0001-Handle-if-TERM-is-not-set.patch
Patch1:         0002-Fix-path-regex-for-and.patch
Patch2:         0003-Fix-failing-to-pasre-par-val-parameters.patch
Patch3:         0004-Fix-failing-to-pasre-param-like-cfgstr-par-val.patch
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires: pyparsing python-urwid python-six

%description
A framework to implement simple but nice configuration-oriented
command-line interfaces.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%{python_sitelib}/*
%doc COPYING README.md

%changelog
* Thu Mar 29 2018 Maurizio Lombardi <mlombard@redhat.com> - 1:1.1.fb23-4
- Fix failure when parsing parameters
- Add 0003-Fix-failing-to-pasre-par-val-parameters.patch
- Add 0004-Fix-failing-to-pasre-param-like-cfgstr-par-val.patch

* Tue May 30 2017 Andy Grover <agrover@redhat.com> - 1:1.1.fb23-3
- Rename configshell-fix-term.patch to 0001*
- Add 0002-Fix-path-regex-for-and.patch

* Tue May 23 2017 Andy Grover <agrover@redhat.com> - 1:1.1.fb23-2
- Add configshell-fix-term.patch

* Thu Mar 2 2017 Andy Grover <agrover@redhat.com> - 1:1.1.fb23-1
- Update to latest in Fedora

* Wed Jul 15 2015 Andy Grover <agrover@redhat.com> - 1:1.1.fb18-1
- Update to latest in Fedora

* Wed Sep 24 2014 Andy Grover <agrover@redhat.com> - 1:1.1.fb14-1
- New upstream release

* Mon Jan 27 2014 Andy Grover <agrover@redhat.com> - 1:1.1.fb11-3
- Update source/URL to current
- Fix changelog

* Mon Jan 6 2014 Andy Grover <agrover@redhat.com> - 1:1.1.fb11-1
- New upstream release

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:1.1.fb9-2
- Mass rebuild 2013-12-27

* Thu Sep 12 2013 Andy Grover <agrover@redhat.com> - 1:1.1.fb9-1
- New upstream release
- Remove dependency on python-simpleparse in favor of pyparsing
- Remove BuildRequires

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.fb8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Andy Grover <agrover@redhat.com> - 1:1.1.fb8-1
- New upstream release
- License now Apache 2.0
- README.md instead of README

* Tue Feb 26 2013 Andy Grover <agrover@redhat.com> - 1:1.1.fb7-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.fb6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 4 2013 Andy Grover <agrover@redhat.com> - 1:1.1.fb6-1
- New upstream release
- Update source URL

* Tue Jul 31 2012 Andy Grover <agrover@redhat.com> - 1:1.1.fb5-1
- New upstream release
- Update Source URL to proper tarball

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.fb4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Andy Grover <agrover@redhat.com> - 1:1.1.fb4-1
- New upstream release

* Wed Dec 14 2011 Andy Grover <agrover@redhat.com> - 1:1.1.fb3-1
- New upstream release

* Tue Dec 13 2011 Andy Grover <agrover@redhat.com> - 1:1.1.fb2-1
- New upstream release

* Tue Dec 6 2011 Andy Grover <agrover@redhat.com> - 1:1.1.fb1-1
- New upstream source and release
- Remove patches:
  * python-configshell-remove-epydoc-dep.patch
  * python-configshell-git-version.patch

* Mon Nov 21 2011 Andy Grover <agrover@redhat.com> - 1:1.1-2
- Properly update changelog
- Sync version with upstream, Epoch used
- Change Source URL to intermediate github repo

* Fri Sep 23 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-5
* Rebuild

* Thu Aug 25 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-4
- Add patch
  - python-configshell-remove-epydoc-dep.patch

* Wed Aug 17 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-3
- Address comments from spec review
  - drop examples/myshell from doc, it hasn't been updated for API change
  - Fully document procedure to generate source .tar.gz
  - Remove "." from summary
  - Remove commented-out spec todos and other cruft

* Mon Aug 1 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-2
- Update to latest git version
- Add urwid builddep

* Tue May 10 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-1
- Initial packaging
