IFS='
'
for i in `scrapy list`; 
do 
	scrapy crawl $i -o data/$i.json
done
