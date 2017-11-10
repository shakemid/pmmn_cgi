# pmmn\_cgi
A Poor Man's Munin Node CGI Wrapper

# Synopsis

A Poor Man's Munin Node (pmmn) is a lite alternative implementation of munin-node. It is designed to work with Perl core modules and ssh+inetd/xinetd. It would be useful especially for old or restricted environment.
- [A Poor Man's Munin Node](https://github.com/munin-monitoring/contrib/tree/master/tools/pmmn)
- [A Poor Man's Munin Node to Monitor "Hostile" UNIX Servers](http://blog.pwkf.org/post/2008/11/04/A-Poor-Man-s-Munin-Node-to-Monitor-Hostile-UNIX-Servers)

pmmn.cgi is CGI wrapper for pmmn. It aims to monitor web servers which can not use ssh but can execute pmmn, for example, shared web hosting services.

# Usage

- Server to monitor
  - Put pmmn and munin plugins on the web server. It would be better to place outside document root.
  - Put pmmn.cgi in some directory which can excecute CGI script. For example, under cgi-bin/.
  - Access control for pmmn.cgi would be a good idea. With Apache httpd, access control with ip address or BASIC auth by using .htaccess would be popular.

- Munin Manager
  - Put pmmnc\_ at munin lib/plugins directory.
  - Make symlink to munin etc/plugins directory. For example, ln -s /path/to/munin/lib/plugins/pmmnc\_ pmmnc\_hostname.
  - Set environment variable env.pmmn\_uri if nesessary.
  - pmmnc\_ behaves like a multi-graph plugin. 

# Lisence

GPLv2
