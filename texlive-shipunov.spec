Name:		texlive-shipunov
Version:	52334
Release:	1
Summary:	A collection of LaTeX packages and classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shipunov
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shipunov.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shipunov.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bst/shipunov
%{_texmfdistdir}/tex/latex/shipunov
%doc %{_texmfdistdir}/doc/latex/shipunov

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
