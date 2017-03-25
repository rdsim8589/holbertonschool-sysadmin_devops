# fix a type in the php
exec { 'correct php typo':
  cwd     => '/var/www/html',
  path    => '/usr/bin:/usr/sbin:bin',
  command => 'sed -i "s/phpp/php/" wp-settings.php',
}
