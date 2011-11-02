Name:		texlive-pgf-umlsd
Version:	0.5
Release:	1
Summary:	Draw UML Sequence Diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-umlsd
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-umlsd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-umlsd.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
LaTeX macros to draw UML diagrams using pgf.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pgf-umlsd/pgf-umlsd.sty
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/README
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/pgf-umlsd-demo.pdf
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/pgf-umlsd-demo.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/pgf-umlsd-demo2.pdf
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/pgf-umlsd-demo2.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
