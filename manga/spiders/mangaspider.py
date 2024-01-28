import scrapy
from ..items import MangaItem

class MangaspiderSpider(scrapy.Spider):
    name = "mangaspider"
    allowed_domains = ["www.supremenepal.com"]
    start_urls = ["https://www.animestore.supremenepal.com/product-category/manga/page/{}".format(page) for page in range(1,5)]

    def parse(self, response): 
        item = MangaItem()
        mangas = response.css(".product-type-simple")

        for manga in mangas:
            manga_title = manga.css(".product-title a::text").get()
            manga_currency = manga.css("span.woocommerce-Price-currencySymbol::text").extract()
            manga_price = [manga.replace('\xa0','') for manga in manga.css("span.price span.woocommerce-Price-amount::text").extract()]
            manga_imageurl = manga.css("img.wp-post-image::attr(src)").get()
            item['manga_title'] = manga_title
            item['manga_price'] = ' '.join(manga_currency+manga_price)
            item['manga_imageurl'] = manga_imageurl
            yield item
        