Summary:	Linux Audio Developer's Simple Plugin API plugin for XMMS
Summary(pl):	Wtyczka Linux Audio Developer's Simple Plugin API dla XMMS-a
Name:		xmms-effect-ladspa
Version:	0.6
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.ecs.soton.ac.uk/~njl98r/code/ladspa/xmms_ladspa-%{version}.tar.gz
# Source0-md5:	b3cd498fa6206910d14a8540ac66f19f
URL:		http://www.ecs.soton.ac.uk/~njl98r/code/ladspa/
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS LADSPA is an Effect for XMMS that provides (some of) the power of
the Linux Audio Developer's Simple Plugin API to your everyday MP3 and
all-around media player.

Normally XMMS can only handle a single Effect, such as Echo and it has
to be written specifically for XMMS. With XMMS LADSPA you can use any
number of audio processing plugins written to the LADSPA
specification, which includes all the GPL software at plugin.org.uk
maintained by Steve Harris.

%description -l pl
XMMS LADSPA to efekt dla XMMS-a dostarczaj±cy (czê¶æ) potêgi LADSPA
(Linux Audio Developer's Simple Plugin API - prostego API dla wtyczek
d¼wiêkowych pod Linuksem) do powszechnie u¿ywanego odtwarzacza
d¼wiêku.

Normalnie XMMS mo¿e obs³u¿yæ tylko pojedyncze efekty, takie jak Echo,
w dodatku napisane specjalnie dla XMMS-a. Przy pomocy XMMS LADSPA
mo¿na u¿ywaæ dowolnej liczby wtyczek przetwarzaj±cych d¼wiêk,
napisanych zgodnie ze specyfikacj± LADSPA - w tym ca³o¶æ
oprogramowania na licencji GPL z plugin.org.uk, utrzymywanego przez
Steve'a Harrisa.

%prep
%setup -q -n xmms_ladspa

%build
%{__cc} -Wall -shared %{rpmcflags} `xmms-config --cflags` -o ladspa.so ladspa.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_effect_plugindir}

install ladspa.so $RPM_BUILD_ROOT%{xmms_effect_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog PLUGINS
%attr(755,root,root) %{xmms_effect_plugindir}/*.so
