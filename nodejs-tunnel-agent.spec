%{?scl:%scl_package nodejs-tunnel-agent}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-tunnel-agent
Version:    0.3.0
Release:    3%{?dist}
Summary:    HTTP proxy tunneling agent
License:    ASL 2.0
URL:        https://github.com/mikeal/tunnel-agent
Source0:    http://registry.npmjs.org/tunnel-agent/-/tunnel-agent-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/tunnel-agent
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/tunnel-agent

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/tunnel-agent
%doc README.md LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.3.0-3
- Add license and readme

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.3.0-2
- replace provides and requires with macro

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-1
- new upstream release 0.3.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2.0-2
- Add support for software collections

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- initial package
