%global tl_name bibleref-french
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4.0
Release:	%{tl_revision}.1
Summary:	French translations for bibleref
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-french
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-french.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-french.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-french.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides translations and alternative typesetting
conventions for use of bibleref in French.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bibleref-french
%dir %{_datadir}/texmf-dist/source/latex/bibleref-french
%dir %{_datadir}/texmf-dist/tex/latex/bibleref-french
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-french/Lacroux-Bible.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-french/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-french/bible.bib
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-french/bibleref-french-francais.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-french/bibleref-french-francais.tex
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-french/bibleref-french.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-french/livres.tex
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-french/makefile
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-french/styles.tex
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-french/test.tex
%doc %{_datadir}/texmf-dist/source/latex/bibleref-french/bibleref-french.dtx
%doc %{_datadir}/texmf-dist/source/latex/bibleref-french/bibleref-french.ins
%{_datadir}/texmf-dist/tex/latex/bibleref-french/bibleref-french.sty
