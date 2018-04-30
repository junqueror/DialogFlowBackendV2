

class DialogFlowWrapper():

    handlers = {}

    @staticmethod
    def call(request):
        type = request['queryResult']['intent']['displayName']
        if type in DialogFlowWrapper.handlers:
            for h in DialogFlowWrapper.handlers[type]:
                h(request)


    @staticmethod
    def event(type):
        def registerhandler(handler):
            if type in DialogFlowWrapper.handlers:
                DialogFlowWrapper.handlers[type].append(handler)
            else:
                DialogFlowWrapper.handlers[type] = [handler]
            return handler

        return registerhandler


