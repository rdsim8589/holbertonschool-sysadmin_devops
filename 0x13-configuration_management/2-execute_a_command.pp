# kill process killmenow
exec {'pkill killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
}
