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

#     - include: tasks_python.yml                          # basic updates to py & pip
#     - include: tasks_worktools.yml                       # swiss knife for desktop utilities

#     - include: tasks_mongodb.yml                         # mongodb 2.6
#     - include: tasks_mysql.yml                           # MYSQL 5.5
#     - include: tasks_percona_toolkit.yml                 # percona tools for mysql


#     - include: tasks_nginx.yml                           # nginx
#     - include: tasks_apache.yml                          # apache prefork|worker

#     - include: tasks_nodejs.yml                          # node 0.10.*
#     - include: tasks_java.yml                            # java 6-7-8
#     - include: tasks_php_apache.yml                      # php 5.5 for apache

#     - include: tasks_jetbrains_phpstorm.yml              # PHP IDE
#     - include: tasks_jetbrains_pycharm_community.yml     # PY IDE
#     - include: tasks_jetbrains_rubymine.yml              # RUBY IDE
#     - include: tasks_jetbrains_intellij_community.yml    # JAVA IDE

#     - include: tasks_robomongo.yml                       # mongo GUI tool    
#     - include: tasks_dbeawer.yml                         # mysql | postgre GUI tool

#     - include: tasks_docker.yml # docker

</pre>

# Defaults

<pre>
    apps_dir: "/home/YOURUSER/apps"
    mysql_root_user: root
    mysql_root_password: devroot
    apache_mode: worker # use prefork or worker variables
    java_version: 8
    phpstorm_version: 9.0.2
    pycharm_version: 4.5.4
    rubymine_version: 7.1.4
    intellij_version: 14.1.4
    robomongo_version: 0.8.5
    dbeawer_version: 3.4.5
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

## Documentation tools
*Tools to ensure your project documentation does not get lost*

* [Apiary](http://apiary.io) Markdown based grammar do describe your REST API
* [Aglio](https://github.com/danielgtaylor/aglio) Custom renderer for apiary based syntax for REST API - zero dependency on apiary itself
* [PlantUML](http://plantuml.com/) - Plain text grammar to describe project UML diagrams
* [Bizagi modeler](http://www.bizagi.com/en/products/bpm-suite/modeler) Bizagi modeler - BMPN2.0 compatible tool for drowing business flow diagrams (Windows only)
* [Gliffy](https://www.gliffy.com/go/commerce/index) html5 based online diagramming tool with BMPN 2.0 support


## #Database tools
*When you are tired of console*

* [DBeawer](http://dbeaver.jkiss.org/) Great tool to work with MySQL, Postgres and bunch or another DBs
* [Robomongo](http://robomongo.org/) Awesome free gui client for MongoDB
* [Common schema](https://github.com/shlomi-noach/common_schema) DBA's framework for MySQL

## Workplace handy tools

* [Midnight Commander](https://www.midnight-commander.org/) visual folder structure browsing
* [Git-Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow/) Git-Flow - +- successful git branching model
* [open in terminal]() action "open in terminal" for Nautilus
* [unzip]() unzip
* [p7zip](http://p7zip.sourceforge.net/) p7zip
* [terminator](https://apps.ubuntu.com/cat/applications/precise/terminator/) terminator
* [sublime](http://www.sublimetext.com/2) sublime text 2
* [atom](https://atom.io/) github's atom editor
* [zeal](https://zealdocs.org/) Zeal offline documentation browser
* [chrome](https://www.google.com/chrome/) Google chrome stable
* [d.pr](http://droplr.com/apps) Cross platform online screenshot capture
client
* [Shutter](http://shutter-project.org/) Unix only screenshot capture

## Collaboration

* [HipChat](https://www.hipchat.com/downloads) Crossplatform atlassian HipChat
* [Slack](https://slack.com/downloads) Crossplatform slack client
* [Appear.in](http://appear.in/) Client-less online multiplatform WebRTC collaboration tool with screen sharing support
* [Speak.io](http://speak.io/) custom video/screen/sound communication for teams. Free unlimited trial period.
* [Teamviewer](https://www.teamviewer.com/en/index.aspx) Most known tool for screen sharing and remote control

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