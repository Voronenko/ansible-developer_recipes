# ansible-developer_recipes
Helper ansible repository for my devbox box configuration. Suitable for: LAMP, MEAN stack, Java stack [DevOps, Ansible]

![pack contents](https://raw.githubusercontent.com/Voronenko/ansible-developer_recipes/master/docs/contents.png)

# Installation as simple, as
- get your brand new ubuntu 14.04 LTS
- install git, curl: sudo apt-get install curl git
- clone repository: git clone git@github.com:Voronenko/ansible-developer_recipes.git
- copy local.yml.template to local.yml
- uncomment portions of software you want to install + adjust variables if needed
- run bootsrap.sh to ensure you have all necessary tools
- run local.sh to provision your box.


# bundled recipes:

<pre>

#     - include: tasks_cleanupubuntu.yml                   # removes games, lens, etc
#     - include: tasks_python.yml                          # basic updates to py & pip
#     - include: tasks_worktools.yml                       # swiss knife for desktop utilities
#     - include: tools/tasks_tmux.yml                      # If you are the tmux fun

#     - include: tasks_mongodb_3.yml                       # mongodb 3.0
#     - include: tasks_mysql.yml                           # MYSQL 5.5
#     - include: tasks_percona_toolkit.yml                 # percona tools for mysql


#     - include: tasks_nginx.yml                           # nginx
#     - include: tasks_apache.yml                          # apache prefork|worker

#     - include: tasks_nodejs.yml                          # node 0.10.* 0.12.*
#     - include: tasks_java.yml                            # java 6-7-8
#     - include: tasks_php_apache.yml                      # php 5.5 for apache
#     - include: tasks_ruby.yml                            # Set system ruby to 2.1

#     - include: tasks_jetbrains_phpstorm.yml              # PHP IDE
#     - include: tasks_jetbrains_pycharm_community.yml     # PY IDE
#     - include: tasks_jetbrains_rubymine.yml              # RUBY IDE
#     - include: tasks_jetbrains_intellij_community.yml    # JAVA IDE

#     - include: tasks_robomongo.yml                       # mongo GUI tool
#     - include: tasks_dbeawer.yml                         # mysql | postgre GUI tool

#     - include: tasks_docker.yml                          # docker

#     - include: tasks_oracle_virtualbox.yml               # Oracle Virtual Box
#     - include: tasks_vagrant.yml                         # Vagrant

#      RUBY
#     - include: ruby/ch_ruby.yml                          # chruby
#     - include: ruby/ruby_install.yml                     # ruby-install
#     - include: ruby/ruby.yml                             # installs ruby itself

#      LAMP
#     - include: lamp/phpdox.yml                            # phpdox documentator
#     - include: lamp/doxygen.yml                           # doxygen documentator
#     - include: lamp/phploc.yml                            # phploc tool
#     - include: lamp/phpcs.yml                             # phpcs tool
#     - include: lamp/phpmd.yml                             # phpmd tool

#     - include: tools/tasks_expect.yml                    # expect tool
#     - include: tools/tasks_plantuml.yml                  # plant uml
#     - include: tools/tasks_toggle.yml                    # toggle time tracker
#     - include: tools/tasks_dpr.yml                       # d.pr screenshoting tool

#     VMWARE
#     - include: vmware/tasks_vmware_tools.yml             # ESX vmware tools

#    DEVELOPMENT
#     - include: tools/tasks_mailhog.yml                    # Web and API based SMTP testing

# COMMUNICATIONS
#     - include: tools/tasks_skype.yml                       # skype 4.3
#     - include: tools/tasks_speak_io.yml                    # speak.io client
#     - include: tools/tasks_slack_client.yml               # slack
#     - include: tools/tasks_hipchat_client.yml             # hipchat

#  TIME TRACKING
#     - include: tools/tasks_toggle.yml

#  DESKTOP shortcuts
#     - include: e531/desktop_icons_pack.yml              # desktop icons
#     - include: e531/shortcuts.yml                       # desktop shortcuts

# Local LAMP debugging
#     - include: vagrant/tasks_vagrant_php_xdebug.yml

# 3rd party code editors
#     - include: tools/tasks_microsoft_visual_studio_code.yml

# 3rd party tools
#     - include: tools/tasks_s3cmd.yml
#     - include: tools/tasks_openshift_rhctools.yml
#     - include: tools/tasks_travis_clienttools.yml

</pre>


# bundled recipes for local or vagrant based LAMP debugging
<pre>

# - include: "{{root_dir}}/vagrant/tasks_vagrant_php_webgrind.yml"                   # Webgrind
# - include: "{{root_dir}}/vagrant/tasks_vagrant_phpmyadmin.yml"                 # PhpMyAdmin
# - include: "{{root_dir}}/vagrant/tasks_vagrant_php_xdebug.yml"                 # XDebug extension
# - include: "{{root_dir}}/vagrant/tasks_vagrant_write_tools.yml"                # db import script, python venv init scripts
# - include: "{{root_dir}}/vagrant/tasks_vagrant_import_mysqldb_databag.yml"     # (re)imports databases from db folder
# - include: "{{root_dir}}/vagrant/tasks_vagrant_apache2_devsites.yml"           # register apache websites on vagrant


</pre>

# Defaults

<pre>
    apps_dir: "/home/YOURUSER/apps"
    mysql_root_user: root
    mysql_root_password: devroot
    apache_mode: worker # use prefork or worker variables
    dbeawer_version: 3.6.3
    chruby_version: 0.3.9
    doxygen_version: 1.8.11
    intellij_version: 2016.1.1 #14.1.4
    java_version: 8
    mailhog_version: 0.1.6
    mongo_version: 3
    monit_version: "5.14-2"
    nodejs_version: "0.12" # 0.10 0.12 4.x 5.x
    oracle_vbox_version: 4.3
    phpstorm_version: "2016.1" # 10.0.3  | "10.0" | 9.0.2 | 8.0.3 | 8.0.1 | 7.1.4 | 6.0.3 | 5.0.4
    php_xdebug_version: 2.2.4
    phpcs_version: 2.5.1
    phpcbf_version: 2.5.1
    pycharm_version: "2016.1" #5.0.1 # 4.5.4
  #    pycharm_edition: community # professional | community
    robomongo_version: 0.8.5
    rubies_location: /opt/rubies
    ruby_install_version: 0.6.0
    option_ruby_install_setsystem: true
    ruby_version: 2.3.0
    rubymine_version: 7.1.4
  #    s3cmd_version: 1.6.1
    travis_version: 1.8.2
    vagrant_version: 1.8.1
    vagrant_plugins:
      - vagrant-vbguest
      - vagrant-hostsupdater
      - vagrant-auto_network

    php_family: default # 5.4 | 5.5 | 5.6 | default
    hypervisor: esx
    # "git-blame" fails to compile with recent atom
    atom_packages: ["angularjs","atom-css-comb", "meteor-api", "emmet", "file-icons", "tag", "expand-region", "atom-alignment", "atom-beautify", "minimap", "set-syntax", "jshint", "linter", "linter-jscs", "jscs-fixer", "highlight-line", "highlight-column", "autocomplete-plus", "toggle-quotes", "monokai"]
</pre>    


## Table of Contents
- [My (awesome) developer recipes](#awesome-developer-recipes)
- [Documentation tools](#documentation tools)
- [Database tools](#Database tools)
- [Workplace handy tools](#Workplace handy tools)
- [Collaboration](#Collaboration)
- [PDF](#PDF)
- [Syncing](#syncing)
- [Awesomes](#Awesomes)
- [Development-LAMP](#Development-LAMP)
- [Development-JS](#Development-JS)
- [Algorithms](#Algorithms)
- [Bookmarklets](#Bookmarklets)


## Databases
* [MySQL](https://www.mysql.com/) MySQL Community  database server
* [MongoDB](https://www.mongodb.org/) Popular NoSQL database [![Build Status](https://travis-ci.org/softasap/sa-mongo.svg?branch=master)](https://travis-ci.org/softasap/sa-mongo)


## Database tools
* [DBeawer](http://dbeaver.jkiss.org/) Great GUI tool to work with MySQL, Postgres and bunch or another DBs [![Build Status](https://travis-ci.org/softasap/sa-dev-dbgui.svg?branch=master)](https://travis-ci.org/softasap/sa-dev-dbgui)

* [Robomongo](http://robomongo.org/) Awesome free gui client for MongoDB [![Build Status](https://travis-ci.org/softasap/sa-dev-dbgui.svg?branch=master)](https://travis-ci.org/softasap/sa-dev-dbgui)

* [Common schema](https://github.com/shlomi-noach/common_schema) DBA's framework for MySQL

## Development

* [Python] Includes most recent packet manager - pip installation and update
* [Java] Installs java runtime environment 6,7, or 8 on the box [![Build Status](https://travis-ci.org/softasap/sa-java.svg?branch=master)](https://travis-ci.org/softasap/sa-java)

* [NodeJS] Installs nodeJS 0.10 or 0.12 with set of most popular tools, including grunt, gulp, bower, npm [![Build Status](https://travis-ci.org/softasap/sa-node.svg?branch=master)](https://travis-ci.org/softasap/sa-node)

* [PHP] Installs PHP for apache or nginx as Fast-CGI [![Build Status](https://travis-ci.org/softasap/sa-lamp.svg?branch=master)](https://travis-ci.org/softasap/sa-lamp)



## Documentation tools
*Tools to ensure your project documentation does not get lost*

* [Apiary](http://apiary.io) Markdown based grammar do describe your REST API
* [Aglio](https://github.com/danielgtaylor/aglio) Custom renderer for apiary based syntax for REST API - zero dependency on apiary itself
* [PlantUML](http://plantuml.com/) - Plain text grammar to describe project UML diagrams
* [GnuPlot](http://gnuplot.sourceforge.net/) - Gnuplot supports many different types of 2D and 3D plots
* [BlockDiag](http://blockdiag.com/en/) - Blockdiag and its family generate diagram images from simple text files
* [Bizagi modeler](http://www.bizagi.com/en/products/bpm-suite/modeler) Bizagi modeler - BMPN2.0 compatible tool for drowing business flow diagrams (Windows only)
* [Gliffy](https://www.gliffy.com/go/commerce/index) html5 based online diagramming tool with BMPN 2.0 support
* [SchemaSpy](http://schemaspy.sourceforge.net/) old but still good documentator for databases
* [SchemaCrawler](http://sualeh.github.io/SchemaCrawler/) Similar to SchemaSpy, under development, but more complex to use
* [Pandoc](https://github.com/jgm/pandoc) Universal markup converter (i.e. docx to rst & so on)

## Virtualization
* [Docker](https://www.docker.com/) Necessary docker components to build and run docker containers locally
* [Oracle Virtual Box](https://www.virtualbox.org/) Free virtualization environment for Linux
* [Vagrant](https://www.vagrantup.com/) Create and configure lightweight, reproducible, and portable development environments
* [ESXi client tools](https://www.vmware.com/products/vsphere-hypervisor) When I work under ESXi - provides better experience


## Webservers
* [Apache](http://www.apache.org/) Classic WebServer (recipe supports both prefork and worker models)
* [Nginx](http://nginx.org/) Compact effective webserver for highload [![Build Status](https://travis-ci.org/softasap/sa-nginx.svg?branch=master)](https://travis-ci.org/softasap/sa-nginx)


## Workplace handy tools

[![Build Status](https://travis-ci.org/softasap/sa-dev-worktools.svg?branch=master)](https://travis-ci.org/softasap/sa-dev-worktools)


* [Midnight Commander](https://www.midnight-commander.org/) visual folder structure browsing
* [Git-Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow/) Git-Flow - +- successful git branching model
* [open in terminal]() action "open in terminal" for Nautilus
* [unzip]() unzip
* [p7zip](http://p7zip.sourceforge.net/) p7zip
* [terminator](https://apps.ubuntu.com/cat/applications/precise/terminator/) terminator
* [tmux](https://github.com/tmux/tmux) tmux
* [sublime](http://www.sublimetext.com/2) sublime text 2
* [atom](https://atom.io/) github's atom editor
* [zeal](https://zealdocs.org/) Zeal offline documentation browser
* [chrome](https://www.google.com/chrome/) Google chrome stable
* [d.pr](http://droplr.com/apps) Cross platform online screenshot capture
client
* [Shutter](http://shutter-project.org/) Unix only screenshot capture


## Development IDE's

* [PHPStorm](https://www.jetbrains.com/phpstorm/) Jetbrains IDE for PHP [![Build Status](https://travis-ci.org/softasap/sa-dev-phpstorm.svg?branch=master)](https://travis-ci.org/softasap/sa-dev-phpstorm)

* [PyCharm](https://www.jetbrains.com/pycharm) Jetbrains IDE for Python [![Build Status](https://travis-ci.org/softasap/sa-dev-pycharm.svg?branch=master)](https://travis-ci.org/softasap/sa-dev-pycharm)

* [Rubymine](https://www.jetbrains.com/ruby/) Jetbrains IDE for Ruby [![Build Status](https://travis-ci.org/softasap/sa-dev-rubymine.svg?branch=master)](https://travis-ci.org/softasap/sa-dev-rubymine)
* [Idea](https://www.jetbrains.com/idea/) Jetbrains IDE for Java [![Build Status](https://travis-ci.org/softasap/sa-dev-intellij.svg?branch=master)](https://travis-ci.org/softasap/sa-dev-intellij)


## Collaboration

* [HipChat](https://www.hipchat.com/downloads) Crossplatform atlassian HipChat
* [Slack](https://slack.com/downloads) Crossplatform slack client
* [Speak.io](http://speak.io/) custom video/screen/sound communication for teams. Free unlimited trial period.
* [Teamviewer](https://www.teamviewer.com/en/index.aspx) Most known tool for screen sharing and remote control
* [Appear.in](http://appear.in/) Client-less online multiplatform WebRTC collaboration tool with screen sharing support

## PDF
* [Bullzip PDF Printer](http://www.bullzip.com/products/pdf/info.php) free PDF printer for windows

## Syncing
* [Sync driver](syncDriver for OneDrive ) Alternative Microsoft OneDrive sync client

## Awesomes

* [MySQL](http://shlomi-noach.github.io/awesome-mysql/) http://shlomi-noach.github.io/awesome-mysql/
* [DevOps](https://github.com/kahun/awesome-sysadmin) https://github.com/kahun/awesome-sysadmin
* [Javascript](https://github.com/sorrycc/awesome-javascript) https://github.com/sorrycc/awesome-javascript
* [Python](https://github.com/vinta/awesome-python) https://github.com/vinta/awesome-python
* [PHP](https://github.com/ziadoz/awesome-php) https://github.com/ziadoz/awesome-php
* [Javascript libraries](http://jster.net/) http://jster.net/ - curated list of libraries

## Development-LAMP
* [PHP QA Tools](http://phpqatools.org/)

## Development-JS
* [CasperJS](http://casperjs.org/) http://casperjs.org/CasperJS is an open source navigation scripting & testing utility written in Javascript for the PhantomJS WebKit headless browser and SlimerJS (Gecko). It eases the process of defining a full navigation scenario and provides useful high-level functions, methods & syntactic sugar

## Algorithms
* [algolist.manual.ru](http://algolist.manual.ru/)
* [Algorithms, 4th Edition(princeton)](http://algs4.cs.princeton.edu/home/)
* [Algorithms in Java](http://underpop.online.fr/j/java/algorithims-in-java-1-4/toc.htm)

## Bookmarklets
* [Yaml debug](http://debug.yaml.de/)
