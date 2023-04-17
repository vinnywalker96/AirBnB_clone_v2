# Configures a web server for deployment of web_static

class nginx_server {
   package { 'nginx':
       ensure => installed,
   }

   service { 'nginx':
       ensure => running,
       enable => true,
       require => Package['nginx'],
   }

   file { '/data/web_static/releases/':
       ensure => directory,
       mode => '0755',
       owner => 'ubuntu',
       group => 'ubuntu',
       recurse => true,
   }
}

include nginx_server
  
