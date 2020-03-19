# -*- coding: utf-8 -*-
import scrapy
import wordcounter
from scrapy import Field, Item, Request
from scrapy.spiders import CrawlSpider, Spider
import lxml.html
from lxml.cssselect import CSSSelector


class ArinItem(Item):
    judul = Field()
    isi = Field()
    link = Field()
    tanggal = Field()
    





class DetikSpider(scrapy.Spider):
    name = 'detik'
    allowed_domains = ['detik.com']
    start_urls = ['https://www.detik.com/search/searchall?query=wisata%20bangka&siteid=3&sortby=time']

    
        

    

    def start_requests(self):
        urls = ['https://www.detik.com/search/searchall?query=wisata%20bangka&siteid=3&sortby=time&page=1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(2, 60):   #159
            urls= response.css('.list.media_rows.list-berita a ::attr("href")').extract()    
            for url in urls:
                global link 
                link = url
                splitted_url = url.split('.')
                if splitted_url[0]=='https://news':
                    yield response.follow(url=url, callback=self.parse_news)   
                # if splitted_url[0]=='https://travel':
                #     yield response.follow(url=url, callback=self.parse_travel)
                # if splitted_url[0]=='https://health':
                #     yield response.follow(url=url, callback=self.parse_health)
                # if splitted_url[0]=='https://wolipop':
                #     yield response.follow(url=url, callback=self.parse_wolipop)   
                # if splitted_url[0]=='https://finance':
                #     yield response.follow(url=url, callback=self.parse_wolipop)   
            next_page_url = 'https://www.detik.com/search/searchall?query=wisata%20bangka&siteid=3&page='
                            
            next_page_url=response.urljoin(next_page_url+str(i))
            yield scrapy.Request(url=next_page_url, callback=self.parse)
    
    def parse_news(self, response):
        item=ArinItem()

        judul = response.xpath(".//h1[contains(@class, 'detail__title')]/text()").extract()
        judul = str(judul).replace('\\n', '')
        judul = judul.replace("'", "")
        judul = judul.replace('[', '')
        judul = judul.replace(']', '')
        item['judul'] = judul

        isi = response.xpath(".//div[@class='detail__body-text']//text()").extract()
        isi = str(isi).replace('\\n', '')
        isi = isi.replace("'", "")
        isi = isi.replace('[', '')
        isi = isi.replace(']', '')
        isi = isi.split()
        isi = ' '.join(isi)
        item['isi'] = isi
        
        global link
        item['link'] = response.url
        
        tanggal = response.xpath(".//div[contains(@class, 'detail__date')]/text()").extract()
        tanggal = str(tanggal).replace("'", "")
        tanggal = tanggal.replace('[', '')
        tanggal = tanggal.replace(']', '')
        item['tanggal'] = tanggal

        yield item

    def parse_travel(self, response):
        item=ArinItem()

        judul = response.xpath(".//h1[contains(@class, 'mt5')]/text()").extract()
        judul = str(judul).replace('\\n', '')
        judul = judul.replace("'", "")
        judul = judul.replace('[', '')
        judul = judul.replace(']', '')
        item['judul'] = judul

        isi = response.xpath(".//p/text()").extract()
        isi = str(isi).replace('\n', '')
        isi = isi.replace('\t', '')
        isi = isi.replace("'", "")
        isi = isi.replace('[', '')
        isi = isi.replace(']', '')
        isi = isi.replace(',', '')
        item['isi'] = isi
        
        global link
        item['link'] = response.url
        
        tanggal = response.xpath(".//div[contains(@class, 'date')]/text()").extract()
        tanggal = str(tanggal).replace("'", "")
        tanggal = tanggal.replace('[', '')
        tanggal = tanggal.replace(']', '')
        item['tanggal'] = tanggal

        yield item

    def parse_health(self, response):
        item=ArinItem()

        judul = response.xpath(".//h1[contains(@class, 'jdl')]/text()").extract()
        judul = str(judul).replace('\\n', '')
        judul = judul.replace("'", "")
        judul = judul.replace('[', '')
        judul = judul.replace(']', '')
        item['judul'] = judul

        isi = response.xpath(".//p/text()").extract()
        isi = str(isi).replace('\n', '')
        isi = isi.replace('\t', '')
        isi = isi.replace("'", "")
        isi = isi.replace('[', '')
        isi = isi.replace(']', '')
        item['isi'] = isi
        
        global link
        item['link'] = response.url
        
        tanggal = response.xpath(".//div[contains(@class, 'date')]/text()").extract()
        tanggal = str(tanggal).replace("'", "")
        tanggal = tanggal.replace('[', '')
        tanggal = tanggal.replace(']', '')
        item['tanggal'] = tanggal

        yield item


    def parse_wolipop(self, response):
        item=ArinItem()

        judul = response.xpath(".//h1[contains(@class, 'jdl')]/text()").extract()
        judul = str(judul).replace('\\n', '')
        judul = judul.replace("'", "")
        judul = judul.replace('[', '')
        judul = judul.replace(']', '')
        item['judul'] = judul

        isi = response.xpath(".//p/text()").extract()
        isi = str(isi).replace('\n', '')
        isi = isi.replace('\t', '')
        isi = isi.replace("'", "")
        isi = isi.replace('[', '')
        isi = isi.replace(']', '')
        item['isi'] = isi
        
        global link
        item['link'] = response.url
        
        tanggal = response.xpath(".//div[contains(@class, 'date')]/text()").extract()
        tanggal = str(tanggal).replace("'", "")
        tanggal = tanggal.replace('[', '')
        tanggal = tanggal.replace(']', '')
        item['tanggal'] = tanggal

        yield item

    def parse_finance(self, response):
        item=ArinItem()

        judul = response.xpath(".//h1[contains(@class, 'jdl')]/text()").extract()
        judul = str(judul).replace('\\n', '')
        judul = judul.replace("'", "")
        judul = judul.replace('[', '')
        judul = judul.replace(']', '')
        item['judul'] = judul

        isi = response.xpath(".//p/text()").extract()
        isi = str(isi).replace('\n', '')
        isi = isi.replace('\t', '')
        isi = isi.replace("'", "")
        isi = isi.replace('[', '')
        isi = isi.replace(']', '')
        item['isi'] = isi
        
        global link
        item['link'] = response.url
        
        tanggal = response.xpath(".//div[contains(@class, 'date')]/text()").extract()
        tanggal = str(tanggal).replace("'", "")
        tanggal = tanggal.replace('[', '')
        tanggal = tanggal.replace(']', '')
        item['tanggal'] = tanggal

        yield item

    def parse2(self, response):
        item=CampaignkitabisaItem()
        item['judul'] = response.xpath(".//div[contains(@class, 'project-header')]/h1[contains(@class, 'page-title')]/text()").extract()[0].strip()
        item['nama'] = response.xpath(".//div[contains(@class, 'campaigner-body')]/span[contains(@class, 'text-14')]/span[contains(@class, 'text-14')]/text()").extract()[0].strip()
        item['target'] = response.xpath(".//div[contains(@class, 'project-collected')]/text()").extract()[1].strip()
        item['terkumpul'] = response.xpath(".//div[contains(@class, 'project-collected')]/h1[contains(@class, 'project-collected__amount')]/text()").extract()[0].strip()
        item['jumlahdonatur'] = response.xpath(".//h3[contains(@class, 'fundraiser__title')]/span[contains(@class, 'fundraiser__count')]/text()").extract()[0].strip()
        item['jumlahshares'] = response.xpath(".//span[contains(@class, 'counter__number')]/text()").extract()
        item['mulai'] = response.xpath(".//div[contains(@class, 'project-report')]/span[contains(@class, 'text-14')]/span[contains(@class, 'text--bold')]/text()").extract()[0].strip()
        video = response.xpath(".//div[contains(@class, 'pwa-story__content')]/iframe/@src").extract()
        item['link_video'] = video

        if "www" in video:
            item['video_existence'] = "Ada"
        else:
            item['video_existence'] = "Tidak Ada"

        item['jumlah_foto'] = len(response.xpath(".//div[contains(@class, 'pwa-story__content')]//img/@src").extract())
        teks = response.xpath(".//div[contains(@class, 'pwa-story__content')]//text()").extract()
        teks = ' '.join(teks)
        teks = teks.strip()
        #item['word'] = teks

        for char in '-.,\n':
            teks = teks.replace(char,' ')
            teks = teks.lower()

        word_list = teks.split()
        count = len(word_list)
        item['word_count'] = count

        linkorg = response.xpath(".//div[contains(@class, 'd-ib')]/img/@src").extract()

        if "https://assets.kitabisa.com/images/icon__verified-org.svg" in linkorg:
            item['status_campaigner']='Organisasi'
        else:
            item['status_campaigner']='Individu'

        item['status_akun'] = response.xpath(".//div[contains(@class, 'campaigner-body')]/small[contains(@class, 'text-12')]/text()").extract()

        indikator = response.xpath("//*[contains(@id, 'project-donatur__dana')]/ul/li[1]/div[2]/div/div/time/text()").extract_first().strip()

        if "Offline Donation" in indikator:
            item['offline_donasi'] = response.xpath("//*[contains(@id, 'project-donatur__dana')]/ul/li[1]/div[2]/div/div/div/b/span/text()").extract_first()
        else:
            item['offline_donasi'] ='0'

        yield item
        
        
    
