# revision 33045
# category Package
# catalog-ctan /graphics/pgf/contrib/pgf-umlsd
# catalog-date 2014-02-24 18:59:18 +0100
# catalog-license gpl
# catalog-version 0.7
Name:		texlive-pgf-umlsd
Version:	0.7
Release:	1
Summary:	Draw UML Sequence Diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-umlsd
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-umlsd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-umlsd.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX macros to draw UML diagrams using pgf.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pgf-umlsd/pgf-umlsd.sty
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/README
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/block.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/call.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/callself.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/customize.log
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/customize.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/distance.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/empty.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/instance.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/message.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/messcall.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/multi-threads-example.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/nested-call.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/no-thread-example.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/non-instantaneous-message.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/postlevel.log
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/postlevel.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/prelevel.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/single-thread-example.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/sync-clock.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/thread.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/threadbias.log
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/demo/threadbias.tex
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/diagrams.pdf
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/logo.png
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/pgf-umlsd-manual.pdf
%doc %{_texmfdistdir}/doc/latex/pgf-umlsd/pgf-umlsd-manual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
