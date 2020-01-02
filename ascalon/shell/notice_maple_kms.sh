#!/bin/bash

project_name="eim"
crawler_name="ascalon.crawler"
spider_place="ascalon/spiders/maple"

cd $HOME/${project_name}/${crawler_name}/${spider_place}

PATH=$PATH:/usr/local/bin:/home/ubuntu/.local/bin
export PATH

echo Action : $PWD
echo $PATH

which python
which scrapy

whoami
date
scrapy crawl notice_maple_kms

echo success
