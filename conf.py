#! /usr/bin/python
import ConfigParser
import string, os, sys
class TradeKeys:
    def __init__(self):
        cf = ConfigParser.ConfigParser()
        cf.read("keys.ini")
        kraken_public = cf.get("kraken", "public")
        kraken_secret = cf.get("kraken", "secret")
        poloniex_public = cf.get("poloniex", "public")
        poloniex_secret = cf.get("poloniex", "secret")
        self.keys_info = {'kraken':{'public':kraken_public,
                                    'secret':kraken_secret
                                    }
, 'poloniex':{'public':poloniex_public,
'secret':poloniex_secret
}
                        };
