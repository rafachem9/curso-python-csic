# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:51:21 2020

@author: Antonio
"""
import requests
url = 'https://covid-19-data.p.rapidapi.com/report/country/all'
pais=input("Introduzca nombre de país: ")

querystring = {"date-format":"YYYY-MM-DD","format":"json","date":"2020-10-01","name":pais}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "TfK79jXk2VmshjfQrBEZHTw2ZyRVp1ve6xIjsnXDNQv218NYSI"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

datos=response.json()
print("Casos confirmados: ",format(datos[0]["provinces"][0]["confirmed"],",d"))
print("Fallecimientos: ",format(datos[0]["provinces"][0]["deaths"],",d"))
print("Casos activos: ",format(datos[0]["provinces"][0]["active"],",d"))