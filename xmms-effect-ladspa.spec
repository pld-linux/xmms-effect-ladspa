Summary:	Linux Audio Developer's Simple Plugin API plugin for xmms.
Summary(pl):	Wtyczka Linux Audio Developer's Simple Plugin API dla xmmsa.
Name:		xmms-effect-ladspa
Version:	0.6
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.ecs.soton.ac.uk/~njl98r/code/ladspa/xmms_ladspa-%{version}.tar.gz
# Source0-md5:	b3cd498fa6206910d14a8540ac66f19f
URL:		http://www.ecs.soton.ac.uk/~njl98r/code/ladspa/
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xmms_plugin_dir	%(xmms-config --effect-plugin-dir)

%description
XMMS LADSPA is an Effect for XMMS that provides (some of) the power of
the Linux Audio Developer's Simple Plugin API to your everyday MP3 and
all-around media player.

Normally XMMS can only handle a single Effect, such as Echo and it has
to be written specifically for XMMS. With XMMS LADSPA you can use any
number of audio processing plugins written to the LADSPA
specification, which includes all the GPL software at plugin.org.uk
maintained by Steve Harris.

%prep
%setup -q -n xmms_ladspa

%build
%{__cc} -Wall -shared %{rpmcflags} `xmms-config --cflags` -o ladspa.so ladspa.c

%install
rm -rf $RPM_BUILD_ROOT

install -D ladspa.so \
	$RPM_BUILD_ROOT%{_xmms_plugin_dir}/ladspa.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog PLUGINS
%attr(755,root,root) %{_xmms_plugin_dir}/*.so
