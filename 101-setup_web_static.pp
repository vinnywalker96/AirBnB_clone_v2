# sets up your web servers for the deployment of web_static. 

#updates ubuntu server
exec {'update server':
    command  => 'apt-get update',
    user => 'root',
    provider => 'shell',
}

# install nginx web server
package { 'nginx':
    ensure   => present,
    provider => 'apt-get',
}

file { '/data/web_static/shared':
    ensure => directory,
    mode => '0755',
    owner => 'ubuntu',
    group => 'ubuntu',
    recurse => true,
}

file { '/data/web_static/releases/test/':
    ensure => directory,
    mode => '0755',
    owner => 'ubuntu',
    group => 'ubuntu',
    recurse => true,
}

file { '/data/web_static/releases/test/index.html':
    content => 'Holberton School',
    require => Package['nginx'],
}
 
file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test/',
}

file { '/etc/nginx/sites-available/default':
    content => "\
    server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	server_name vestec.tech;
	root /var/www/html;
	
	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html index.htm;
	}

	location /redirect_me {
		return 301 https://github.com/vinnywalker96;
	}

	error_page 404 /404.html;
	location = /404.html{
		internal;
	}
    }",
    require => Package['nginx'],
    notify => Servive['nginx'],
}

service { 'nginx':
    ensure => 'running',
    enable => true,
    require => Package['nginx'],
}
