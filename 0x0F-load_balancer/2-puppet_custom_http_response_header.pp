# Using Puppet, configure two servers
exec {'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin:/usr/sbin:/bin',

}

package { 'nginx':
  ensure   => installed,
  provider => ['apt'],
  require  => Exec['apt-update'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['default'],
  require   => Package['nginx'],
}

file { 'index.html':
  ensure  => file,
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}
file {'default':
  ensure  => file,
  path    => '/etc/nginx/sites-available/default',
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
      add_header x-served-by ${hostname};
    }
    location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
  }",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  require => Package['nginx'],
  notify  => Service['nginx'],
}