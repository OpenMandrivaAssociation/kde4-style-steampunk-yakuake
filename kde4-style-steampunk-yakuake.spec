Summary:	"SteampunK Powered Linux" Yakuake theme
Name:		kde4-style-steampunk-yakuake
Version:	3.0
Release:	2
License:	Creative Commons Attribution-ShareAlike
Group:		Graphical desktop/KDE
Url:		http://kde-look.org/content/show.php?content=158529
Source0:	http://kde-look.org/CONTENT/content-files/158529-SteampunK.tar.gz
Requires:	yakuake
BuildRequires:	kde4-macros
BuildArch:	noarch

%description
This package contains the "SteampunK Powered Linux" theme for Yakuake.

%files
%{_kde_appsdir}/yakuake/skins/SteampunK

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}%{_kde_appsdir}/yakuake/skins

cp -r SteampunK %{buildroot}%{_kde_appsdir}/yakuake/skins/
