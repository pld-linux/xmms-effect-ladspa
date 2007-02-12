Summary:	Linux Audio Developer's Simple Plugin API plugin for XMMS
Summary(pl.UTF-8):	Wtyczka Linux Audio Developer's Simple Plugin API dla XMMS-a
Name:		xmms-effect-ladspa
Version:	1.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.ecs.soton.ac.uk/~njl98r/code/ladspa/xmms_ladspa-%{version}.tar.gz
# Source0-md5:	5f14d62145188d38008c4e30194916e6
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

%description -l pl.UTF-8
XMMS LADSPA to efekt dla XMMS-a dostarczający (część) potęgi LADSPA
(Linux Audio Developer's Simple Plugin API - prostego API dla wtyczek
dźwiękowych pod Linuksem) do powszechnie używanego odtwarzacza
dźwięku.

Normalnie XMMS może obsłużyć tylko pojedyncze efekty, takie jak Echo,
w dodatku napisane specjalnie dla XMMS-a. Przy pomocy XMMS LADSPA
można używać dowolnej liczby wtyczek przetwarzających dźwięk,
napisanych zgodnie ze specyfikacją LADSPA - w tym całość
oprogramowania na licencji GPL z plugin.org.uk, utrzymywanego przez
Steve'a Harrisa.

%prep
%setup -q -n xmms_ladspa-%{version}

%build
#fix small problem in ver 1.0
sed 's/"LADSPA host " VERSION/"LADSPA host 1.0"/' ladspa.c > ladspa.c.tmp
mv -f ladspa.c.tmp ladspa.c

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
