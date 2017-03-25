# fix a type in the php
exec { 'correct php typo':
  path    => '/usr/bin/:/usr/sbin/:/bin/',
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
}
