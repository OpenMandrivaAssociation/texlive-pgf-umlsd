%global tl_name pgf-umlsd
%global tl_revision 55342

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Draw UML Sequence Diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-umlsd
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-umlsd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-umlsd.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(latex)
Requires:	texlive(pgf)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX macros to draw UML diagrams using pgf

