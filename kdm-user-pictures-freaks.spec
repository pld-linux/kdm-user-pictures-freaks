#$Revision: 1.3 $, $Date: 2007-02-13 08:06:37 $

%define         _name Freaks

Summary:	kdm user pictures - %{_name}
Summary(pl.UTF-8):	Obrazki użytkowników dla kdm-a - %{_name}
Name:		kdm-user-pictures-%{_name}
Version:	01
Release:	1
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/content/files/25210-%{_name}.tar.gz
# Source0-md5:	dbc46c4a97a644358ab1ebee69bb12ed
URL:		http://www.kde-look.org/content/show.php?content=25210
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is icons of user avantars for kdm.

%description -l pl.UTF-8
%{_name} to ikony obrazków użytkowników dla kdm-a.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/%{_name}
install KDM/*.png $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/pics/users/%{_name}
