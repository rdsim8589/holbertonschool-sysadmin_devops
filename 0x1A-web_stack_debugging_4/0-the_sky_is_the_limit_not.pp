#changes ulimit of nginx and restarts the service
$str = '# Note: You may want to look at the following page before setting the ULIMIT.
#  http://wiki.nginx.org/CoreModule
#worker_rlimit_nofile
# Set the ulimit variable if you need defaults to change.
#  Example: ULIMIT="-n 4096"
ULIMIT="-n 4096"'

file { '/etc/default/nginx':
  ensure  => file,
  path    => '/etc/default/nginx',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => '$str',
}
exec { 'nginx':
      command => '/etc/init.d/nginx restart'
}
