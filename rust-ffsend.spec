# Generated by rust2rpm 13
%bcond_without check
%global __cargo_skip_build 0

%global crate ffsend

Name:           rust-%{crate}
Version:        0.2.58
Release:        2%{?dist}
Summary:        Easily and securely share files from the command line

# Upstream license specification: GPL-3.0
License:        GPLv3
URL:            https://crates.io/crates/ffsend
Source:         %{crates_source}
# Initial patched metadata
# * Only linux dependencies
Patch0:         ffsend-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Easily and securely share files from the command line. A fully featured Firefox
Send client.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
Recommends:     xsel

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/ffsend
%{_bindir}/ffput
%{_bindir}/ffget
%{_bindir}/ffdel
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/ffsend.bash
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/ffsend.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_ffsend

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
for t in ffput ffget ffdel; do
  ln -s ffsend %{buildroot}%{_bindir}/$t
done
%{buildroot}%{_bindir}/ffsend generate completions bash fish zsh
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  ffsend.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  ffsend.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  _ffsend

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Josh Stone <jistone@redhat.com> - 0.2.58-1
- Update to 0.2.58

* Thu Dec 05 15:35:44 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.57-1
- Update to 0.2.57
- Add completions

* Thu Dec 05 14:25:19 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.56-1
- Update to 0.2.56

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 12:11:38 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.49-1
- Update to 0.2.49

* Sat Jun 22 13:13:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.48-1
- Update to 0.2.48

* Fri May 31 2019 Josh Stone <jistone@redhat.com> - 0.2.46-2
- Fix symlinks to ffsend

* Sat May 04 21:34:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.46-1
- Update to 0.2.46

* Fri Apr 19 08:17:44 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.45-1
- Update to 0.2.45

* Sat Apr 06 11:08:58 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.44-1
- Update to 0.2.44

* Tue Apr 02 2019 Josh Stone <jistone@redhat.com> - 0.2.43-1
- Update to 0.2.43

* Wed Mar 27 10:57:05 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.42-1
- Update to 0.2.42

* Sat Mar 23 20:08:56 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.39-1
- Update to 0.2.39

* Wed Mar 20 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.38-2
- Drop unneeded BuildRequires

* Wed Mar 20 2019 Josh Stone <jistone@redhat.com> - 0.2.38-1
- Update to 0.2.38

* Tue Mar 19 21:58:14 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.37-1
- Update to 0.2.37

* Sun Mar 17 22:33:08 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.36-1
- Update to 0.2.36

* Sat Mar 16 18:08:50 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.34-1
- Update to 0.2.34

* Fri Mar 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.33-1
- Update to 0.2.33

* Thu Mar 14 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.30-1
- Initial package
