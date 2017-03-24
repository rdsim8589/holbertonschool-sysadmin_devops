# install puppet-lint
package { 'puppet-lint':
  ensure   => 'latest',
  provider => 'gem',
}
