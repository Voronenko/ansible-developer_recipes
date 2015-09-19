# ansible-developer_recipes
Helper ansible repository for my devbox box configuration. Suitable for: LAMP, MEAN stack, Java stack [DevOps, Ansible]

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
#     - include: tasks_php_apache.yml # php 5.5 for apache

#     - include: tasks_jetbrains_phpstorm.yml              # PHP IDE 
#     - include: tasks_jetbrains_pycharm_community.yml     # PY IDE 
#     - include: tasks_jetbrains_rubymine.yml              # RUBY IDE
#     - include: tasks_jetbrains_intellij_community.yml    # JAVA IDE

#     - include: tasks_robomongo.yml                       # mongo GUI tool    
#     - include: tasks_dbeawer.yml                         # mysql | postgre GUI tool

#     - include: tasks_docker.yml # docker

</pre>
