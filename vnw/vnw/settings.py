BOT_NAME = 'vnw'
BOT_VERSION = '1.0.5'

SPIDER_MODULES = ['vnw.spiders']
NEWSPIDER_MODULE = 'vnw.spiders'
ITEM_PIPELINES = {
        'vnw.pipelines.APIPipeline': 1000,
}

USER_AGENT = ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,"
              " like Gecko) Chrome/48.0.2564.116 Safari/537.36")

# VIETNAMWORK_USERNAME = ''
# VIETNAMWORK_PASSWORD = ''
