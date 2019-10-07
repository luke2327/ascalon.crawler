#!/bin/bash

project_name="eim"
crawler_name="ascalon.crawler"
spider_place="ascalon/spiders/vod"

cd $HOME/${project_name}/${crawler_name}/${spider_place}

PATH=$PATH:/usr/local/bin
export PATH

echo Action : $PWD
echo $PATH
whoami
date
scrapy crawl vod_youtube_maple

echo success
