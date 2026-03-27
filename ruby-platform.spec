# NOTE:
# http://rubygems.org/gems/Platform and http://rubygems.org/gems/platform are different gems
# if you're seeking for "platform", then package it as ruby-rails-platform!
%define	gem_name	Platform
Summary:	Naive platform detection for Ruby
Name:		ruby-platform
Version:	0.4.2
Release:	1
License:	LGPL v2+
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{gem_name}-%{version}.gem
# Source0-md5:	0d1ae1cfb5c929694990cbcbf0d6859b
URL:		http://rubyforge.org/projects/platform/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Platform is a library which figures out what platform Ruby is running
on. It's doing the obvious thing of parsing RUBY_PLATFORM but doing it
systematically and it is being tested to make sure it handles 99% of
cases right.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{gem_name}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_vendorlibdir}/platform.rb
%{ruby_specdir}/%{gem_name}-%{version}.gemspec
