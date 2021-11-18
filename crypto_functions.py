import os
from requests import Session, Request
import pprint
import json
#CMC_API_KEY=os.environ.get('CMC')
parameters={
        'start':1,
        'limit':5000
    }

headers={
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':'472ddbe3-0acb-435f-8fba-8fa1954a607e'
    }
session=Session()
session.headers.update(headers)
url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
response=session.get(url,params=parameters)
json_file=json.loads(response.text)['data']
slug_to_id = {d['slug']: d['id'] for d in json_file}

def get_crypto_price(crypto):

    parameters={
        'slug':crypto,
        'convert':'USD'
        }
    url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    response=session.get(url,params=parameters)
    json_file=json.loads(response.text)
        
    Crypto_price=json_file['data'][str(slug_to_id[crypto])]['quote']['USD']['price']
    return f"{crypto.title()}'s price is: {str(Crypto_price)[0:8]}$ "

def get_crypto_rank(crypto):
        CMC_API_KEY=os.environ.get('CMC')
        parameters={
                
                'start':1,
                'limit':5000
                }
        url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
        response=session.get(url,params=parameters)
        json_file=json.loads(response.text)['data']
        slug_to_rank = {d['slug']: d['rank'] for d in json_file}
        return slug_to_rank[crypto.lower()]

def get_crypto_rank2(crypto):
        CMC_API_KEY=os.environ.get('CMC')
        parameters={
                
                'start':1,
                'limit':5000
                }
        url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
        response=session.get(url,params=parameters)
        json_file=json.loads(response.text)['data']
        rank_to_slug = {d['rank']: d['slug'] for d in json_file}
        return rank_to_slug[int(crypto)]

    



def get_price_with_symbol(crypto):

    parameters={
        'symbol':crypto,
        'convert':'USD'
        }

    url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    response=session.get(url,params=parameters)
    json_file=json.loads(response.text)
        
    Crypto_price=json_file['data'][crypto]['quote']['USD']['price']
    return f"{crypto}'s price is: {Crypto_price}$ "
def get_performance_24(crypto):

    parameters={
        'slug':crypto,
        'convert':'USD'
        }
    url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    response=session.get(url,params=parameters)
    json_file=json.loads(response.text)
        
    Crypto_performance=json_file['data'][str(slug_to_id[crypto])]['quote']['USD']["percent_change_24h"]
    if str(Crypto_performance)[0]=='-':
        return f"{crypto} is down {Crypto_performance}%  "
    else:
        return f"{crypto} is up {Crypto_performance}%"
def get_performance_7d(crypto):
    
    parameters={
        'slug':crypto,
        'convert':'USD'
        }
    url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    response=session.get(url,params=parameters)
    json_file=json.loads(response.text)
        
    Crypto_performance=json_file['data'][str(slug_to_id[crypto])]['quote']['USD']["percent_change_7d"]
    if str(Crypto_performance)[0]=='-':
        return f"{crypto} is down {Crypto_performance}%  "
    else:
        return f"{crypto} is up {Crypto_performance}%"

def get_everything_about_the_crypto(crypto):
    parameters={
        'slug':crypto,
        'convert':'USD'
        }
    url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    response=session.get(url,params=parameters)
    json_file=json.loads(response.text)
    crypto_info=json_file['data'][str(slug_to_id[crypto])]['quote']['USD']
    crypto_list= [(key+" : "+str(value)) for key,value in crypto_info.items()]
    return "\n".join(crypto_list)

def get_crypto_info(crypto):
    parameters={'slug':crypto,}
    url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
    response=session.get(url,params=parameters)
    json_file=json.loads(response.text)
    crypto_description=json_file['data'][str(slug_to_id[crypto])]['description']
    return crypto_description


def get_crypto_reddit(crypto):
    parameters={'slug':crypto.lower()}

    url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
    response=session.get(url,params=parameters)
    json_file=json.loads(response.text)
    crypto_description=json_file['data'][str(slug_to_id[crypto])]['urls']['reddit']
    for link in crypto_description:
        return link

def get_crypto_price_in_numbers_only(crypto):

    parameters={
        'slug':crypto,
        'convert':'USD'
        }

    url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    response=session.get(url,params=parameters)
    json_file=json.loads(response.text)
        
    Crypto_price=json_file['data'][str(slug_to_id[crypto])]['quote']['USD']['price']
    return str(Crypto_price)[:7]
    


def get_top10():
    parameters={
                'start':1,
                'limit':5000
                }    
    url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    response=session.get(url,params=parameters)
    json_file=json.loads(response.text)['data']
    top10_rank_to_slug = {d['rank']: d['slug'] for d in json_file}
    top_10 = sorted(top10_rank_to_slug.items())[:10]
    top10_dict={key:value for key,value in top_10}
    
    #top10_string=json.dumps(top10_dict).replace(',', '\n')
    return top10_dict

    



