# revision 27098
# category Package
# catalog-ctan /macros/latex/contrib/bibleref-french
# catalog-date 2012-07-14 16:43:20 +0200
# catalog-license lppl1.3
# catalog-version 2.3.1
Name:		texlive-bibleref-french
Version:	2.3.1
Release:	1
Summary:	French translations for bibleref
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-french
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-french.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-french.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-french.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides translations and alternative typesetting
conventions for use of bibleref in French.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibleref-french/bibleref-french.sty
%doc %{_texmfdistdir}/doc/latex/bibleref-french/Lacroux-Bible.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref-french/bibleref-french-francais.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref-french/bibleref-french-francais.tex
%doc %{_texmfdistdir}/doc/latex/bibleref-french/bibleref-french.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref-french/inclus/bible.bib
%doc %{_texmfdistdir}/doc/latex/bibleref-french/inclus/livres.tex
%doc %{_texmfdistdir}/doc/latex/bibleref-french/inclus/styles.tex
%doc %{_texmfdistdir}/doc/latex/bibleref-french/makefile
%doc %{_texmfdistdir}/doc/latex/bibleref-french/test.tex
#- source
%doc %{_texmfdistdir}/source/latex/bibleref-french/bibleref-french.dtx
%doc %{_texmfdistdir}/source/latex/bibleref-french/bibleref-french.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
