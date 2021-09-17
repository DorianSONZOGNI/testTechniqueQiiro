# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from user_agents import parse
import webbrowser

#return le texte html à afficher ainsi que l'image et son chemin
def buildHtmlMessage():
    try:
        response = requests.get("https://random-data-api.com/api/internet_stuff/random_internet_stuff")
        response.raise_for_status()
    except requests.HTTPError:
        return "error"
    
    #Pour tester avec un userAgent d'android, décommenter la ligne 20 et commenter la ligne 23
    #user_agent = parse("Mozilla/5.0 (Linux; Android 4.0.4; LT30p Build/7.0.A.3.195) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19")
    
    response = response.json()
    user_agent = parse(response['user_agent'])
    
    username = response['username']
    email = response['email']
    
    return "L'adresse email de l'utilisateur <b>"+ username +"</b> est <b>"+ email +"</b>. Il utilise le système d'exploitation <img src=\"img/"+detectOS(user_agent.os.family)+".png\">."

#return le nom des images à afficher
def detectOS(osDetected):
    if('Windows' == osDetected):
        return 'win'
    elif('Mac OS X' == osDetected):
        return 'mac'
    elif('Android' == osDetected):
        return 'and'
    elif('Ubuntu' == osDetected):
        return 'lin'

#construit la page html et l'ouvre dans un navigateur
def createHtmlPage():
    bodyContent = buildHtmlMessage()
    
    if(bodyContent != "error"):
        buildhtml = open('result.html','w')
        
        message = "<html><head></head><body><p>"+bodyContent+"</p></body></html>"
        buildhtml.write(message)
        buildhtml.close()
        
        webbrowser.open_new_tab('result.html')

createHtmlPage()


