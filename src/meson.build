module_keepalive = shared_module('module-keepalive',
  ['keepalive.c', 'module-keepalive.c'],
  include_directories : [configinc],
  c_args : [pa_c_args],
  install : true,
  install_dir : modlibexecdir,
  dependencies : [dbus_dep, pulsecore_dep],
  name_prefix : ''
)
