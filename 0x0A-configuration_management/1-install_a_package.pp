# Using Puppet, install flask from pip3
package {'/usr/bin/python3':
  ensure   => 'installed',
  name     => 'python3',
  provider => 'apt',


}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['/usr/bin/python3'],
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['/usr/bin/python3'],

}

