from flask_assistant import ask
import random

from DialogFlow.dialogFlowWrapper import DialogFlowWrapper

class Default:

    @DialogFlowWrapper.event('Default Welcome Intent')
    def sayHello(request):
        basicResponses = ['¡Hola! 🤖 Soy un asistente virtual y te voy a ayudar con tus compras!!',
                          '¡Hey! 🤖 Soy un asistente virtual y me encantaría ayudarte a elegir tus productos',
                          '¡Buenos días! 🤖 Soy un asistente virtual, y soy especialista en compras online']
        response = ask(random.choice(basicResponses))
        return response