#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json, codecs

params = (
    ('loteria', 'megasena'),
    ('token', 'oRQUQhXAau7JY7G'),
)

#Algum motivo User-Agent default do modulo requests nao funfa, entao tive que usar do firefox
headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0", "Accept-Encoding":"gzip, deflate, br", "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3", "Content-Type":"application/json; charset=utf-8"}

r = requests.get('https://apiloterias.com.br/app/resultado', params=params, headers=headers)
r.encoding
print r.content
d = r.content
data = d.decode("utf-8")
content = json.loads(data)
print content
