# Using Puppet, configure two servers 
exec {'apt-update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure   => installed,
}
-> file_line { 'add-header':
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _',
  line   => "add_header X-Served-By ${hostname}",
}
-> exec { 'restart-service':
  command  => '/usr/sbin/service nginx restart',
}
