
from http.server import BaseHTTPRequestHandler


from urllib import parse
from webbrowser import get
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        api_path=self.path
        url_components=parse.urlsplit(api_path)
        query=parse.parse_qsl(url_components.query)
        dic_set=dict(query)
        self.wfile.write(str(dic_set).encode())
       

        # if dic_set['country']:
        #     country=dic_set['country']
        #     r=requests(url_country+country)
        #     data=r.json()
        #     capital=data[0]['capital'][0]
            
            # self.wfile.write(str(f'capital of {country}is {capital}').encode())
        
        # elif dic_set['capital']:
                
        # else:

        #     self.wfile.write(str(f'').encode())
        if 'country' in dic_set:
            url='https://restcountries.com/v3.1/name/'
            country=dic_set['country']
            r = requests.get(url + country)
            data = r.json()
            capital=data[0]['capital'][0]
            message=f"The capital of {country} is {capital}"
        elif 'capital' in dic_set:
            url='https://restcountries.com/v3.1/capital/'
            capital=dic_set['capital']
            r = requests.get(url + capital)
            data = r.json()
            country= data[0]['name']['common']
            message=f"{capital} is the capital of {country}."

        else:
            message = " no result was found , please try again "
       

        self.wfile.write(message.encode())

        return