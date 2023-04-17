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

   file { '/data':
       ensure => directory,
   }
   file { '/data/web_static':
       ensure => directory,
   }
   file { '/data/web_static/releases':
        ensure => directory,
   }
   file { '/data/web_static/releases/test':
        ensure => directory,
   }
   file { '/data/web_static/shared':
        ensure => directory,
   }
   exec { 'chown -R ubuntu /data/':
        path => '/usr/bin/:/usr/local/bin/:bin/'
   }
   exec { 'chgrp -R ubuntu /data/':
        path => '/usr/bin/:/usr/local/bin/:/bin/'
   }
}

include nginx_server
  
