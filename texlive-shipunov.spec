# revision 24203
# category Package
# catalog-ctan /macros/latex/contrib/shipunov
# catalog-date 2010-10-26 16:14:45 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-shipunov
Version:	1.1
Release:	3
Summary:	A collection of LaTeX packages and classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shipunov
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shipunov.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shipunov.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle collects packages and classes, along with one
bibliography style and examples and scripts for converting TeX
files. Many of the files in the collection are designed to
support field biologists and/or Russian writers, while others
have wider application. The collection includes (among others):
- altverse, a simple verse typesetting package; - autolist,
which provides various list formatting facilities; - biokey,
which provides a mechanism for typesetting biological
identification lists; - biolist, which typesets species lists;
- boldline, which typesets heavier separating lines in tables;
- cassete, which lays out audio cassette inserts; - classif2,
which typesets classification lists; - drcaps, which provides
dropped capital macros; - etiketka, a class for typesetting
business-card-sized information (including business cards); -
flower, for typesetting lists of flower formulae; - isyntax; -
numerus; - punct; - sltables, which develops on the stables
package, for use in a LaTeX context; and - starfn.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/shipunov/rusnat.bst
%{_texmfdistdir}/scripts/shipunov/biokey2html.bat
%{_texmfdistdir}/scripts/shipunov/biokey2html.sh
%{_texmfdistdir}/scripts/shipunov/biokey2html1.pl
%{_texmfdistdir}/scripts/shipunov/biokey2html2.pl
%{_texmfdistdir}/scripts/shipunov/biokey2html3.pl
%{_texmfdistdir}/tex/latex/shipunov/altverse.sty
%{_texmfdistdir}/tex/latex/shipunov/autolist.sty
%{_texmfdistdir}/tex/latex/shipunov/biokey.sty
%{_texmfdistdir}/tex/latex/shipunov/biolist.sty
%{_texmfdistdir}/tex/latex/shipunov/boldline.sty
%{_texmfdistdir}/tex/latex/shipunov/cassete.cls
%{_texmfdistdir}/tex/latex/shipunov/classif2.sty
%{_texmfdistdir}/tex/latex/shipunov/drcaps.sty
%{_texmfdistdir}/tex/latex/shipunov/etiketka.cls
%{_texmfdistdir}/tex/latex/shipunov/flower.sty
%{_texmfdistdir}/tex/latex/shipunov/isyntax.sty
%{_texmfdistdir}/tex/latex/shipunov/numerus.sty
%{_texmfdistdir}/tex/latex/shipunov/punct.sty
%{_texmfdistdir}/tex/latex/shipunov/sltables.sty
%{_texmfdistdir}/tex/latex/shipunov/starfn.sty
%doc %{_texmfdistdir}/doc/latex/shipunov/NEWS
%doc %{_texmfdistdir}/doc/latex/shipunov/README
%doc %{_texmfdistdir}/doc/latex/shipunov/altverse-ex-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/altverse-ex-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/altverse-ex1-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/altverse-ex1-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/altverse-ex2-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/altverse-ex2-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/autolist-ex-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/autolist-ex-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/autolist-ex-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/autolist-ex-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/biokey-doc-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/biokey-doc-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/biokey2html-doc-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/biokey2html-doc-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/biokey2html-ex-en.html
%doc %{_texmfdistdir}/doc/latex/shipunov/biokey2html-ex-en1.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/biokey2html-ex-en2.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/biolist-ex-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/biolist-ex-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/boldline-ex-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/boldline-ex-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/cassete-ex-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/cassete-ex-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/classif2-ex-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/classif2-ex-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/drcaps-ex-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/drcaps-ex-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/etiketka-ex-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/etiketka-ex-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/etiketka-ex1-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/etiketka-ex1-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/etiketka-ex2-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/etiketka-ex2-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/field-form-ex1-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/field-form-ex1-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/field-form-ex2-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/field-form-ex2-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/flower-ex-en-x.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/flower-ex-en-x.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/flower-ex-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/flower-ex-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/isyntax-ex-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/numerus-ex-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/numerus-ex-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/punct-ex-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/punct-ex-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/rusnat-doc-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/rusnat-doc-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/rusnat-ex-ru.bib
%doc %{_texmfdistdir}/doc/latex/shipunov/rusnat-ex1-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/rusnat-ex1-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/rusnat-ex2-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/rusnat-ex2-ru.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/sltables-doc-en.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/sltables-doc-en.tex
%doc %{_texmfdistdir}/doc/latex/shipunov/starfn-ex-ru.pdf
%doc %{_texmfdistdir}/doc/latex/shipunov/starfn-ex-ru.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex scripts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 755981
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719524
- texlive-shipunov
- texlive-shipunov
- texlive-shipunov
- texlive-shipunov

