from flask_assistant import ask
import random

from DialogFlow.dialogFlowWrapper import DialogFlowWrapper
from DataBase.dbController import DbController
from DataBase.DataModels import *

class Smartphones:

    @DialogFlowWrapper.event('product.category>sp.range')
    def askRange(productCategory):
        # context_manager.add(productCategory)
    
        if productCategory == 'Smartphone':
    
            basicResponses = ['¿Qué categoría de móvil estás buscando?',
                              '¿Qué rango de SmartPhones te interesa?',
                              'Elije una de las siguientes gamas para poder empezar',
                              'Lo primero es elegir la gama de SmartPhones que buscamos. Ten encuenta que de esta decisión depende bastante el precio, por lo que te recomiendo que elijas de acuerdo a tus necesidades reales. No queremos gastar dinero en algo que no necesitamos!']
            ranges = DbController.instance().getAll(Range)
            response = ask(random.choice(basicResponses)).build_carousel()
    
            for range in ranges:
                response.add_item(title=range.name, key=range.name, description=range.description)
        else:
            response = ask('Lo siento, pero ahora mismo solo puedo ayudarte con la categoría de SmartPhones.')
    
        return response
    

    @DialogFlowWrapper.event('sp.range>screen')
    def askScreen(smartphoneRange):
        # context_manager.add('smartphone')
    
        basicResponses = [
            'Vamos a empezar por las dimensiones del SmartPhone, que dependen principalmente del tamaño de pantalla.',
            'Las dimensiones del SmartPhone determinan su tamaño. ¿Qué tamaño de pantalla estás buscando?']
        range = DbController.instance().getOneByName(Range, smartphoneRange)
    
        response = ask(random.choice(basicResponses)).build_carousel()
        for screen in range.screens:
            response.add_item(title=screen.name, key=screen.name, description=screen.description)
    
        return response
    

    @DialogFlowWrapper.event('sp.screen>RAM')
    def askRAM(smartphoneScreen):
        print("IN sp.screen>RAM")
        # smartphoneRange = context_manager.get('smartphone', 'smartphoneRange')
        print(smartphoneScreen)
        # print(smartphoneRange)
    
        return ask('In sp.screen>RAM')
    
    
    @DialogFlowWrapper.event('smartphoneCard')
    def showSmartphoneCard(request):
        smartphoneBrand = request['queryResult']['parameters']['smartphoneBrand']
        smartphoneName = request['queryResult']['parameters']['smartphoneName']
        # smartphoneRange = context_manager.get('smartphone', 'smartphoneRange')
    
        smartphone = DbController.instance().getOneByCompanyAndName(SmartPhone, smartphoneBrand, smartphoneName)
    
        response = ask('Aquí lo tienes:')
        response.card(title="{0} {1}".format(smartphone.company, smartphone.name),
                      link=smartphone.officialURL,
                      linkTitle='Web oficial',
                      text="Precio medio: {0!s}€".format(smartphone.avgPrice),
                      img_url=smartphone.image)
    
        # context_manager.add('smartphone')
    
        return response