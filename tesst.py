from shopee_crawler import Crawler

crawler = Crawler()
crawler.set_origin(origin="shopee.vn") # Input your root Shopee website of your country that you want to crawl

data = crawler.crawl_by_shop_url(shop_url='shop_url')

data = crawler.crawl_by_cat_url(cat_url='cat_url')

data = crawler.crawl_by_search(keyword='keyword')

data = crawler.crawl_cat_list()
# print(data)