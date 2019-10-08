AM_LIBADD = \
	$(PULSEAUDIO_LIBS) \
	$(DBUS_LIBS)

AM_CFLAGS = \
	$(PULSEAUDIO_CFLAGS) \
	$(DBUS_CFLAGS)

modlibexec_LTLIBRARIES = \
	module-keepalive.la

noinst_HEADERS = module-keepalive-symdef.h keepalive.h

module_keepalive_la_SOURCES = keepalive.c module-keepalive.c
module_keepalive_la_LDFLAGS = -module -avoid-version -Wl,-z,noexecstack
module_keepalive_la_LIBADD = $(AM_LIBADD)
module_keepalive_la_CFLAGS = $(AM_CFLAGS)
