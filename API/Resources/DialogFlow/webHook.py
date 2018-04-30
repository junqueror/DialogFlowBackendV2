import logging
import traceback
from pprint import pprint
from flask import request
from flask_restplus import Resource
from Application.flaskWrapper import FlaskWrapper
from DialogFlow.Intents.default import *
from DialogFlow.dialogFlowWrapper import DialogFlowWrapper


@FlaskWrapper.Namespaces.dialogflow.route('/webhook')
class WebHookResource(Resource):

    # POST
    @FlaskWrapper.Api.doc('POST for DialogFlow requests')
    @FlaskWrapper.Api.response(200, 'Success')
    @FlaskWrapper.Api.response(400, 'Parameter validation Error')
    def post(self):

        # Get the parameters included in the request
        requestData = request.json

        # Initialize response
        succeed = False
        errorMessage = ''

        try:
            pprint(requestData)

            DialogFlowWrapper.call(requestData)

            # Response parameters
            succeed = True

        except Exception as e:
            logging.error("There was an issue on DialogFlow WebHook: ({0}) : {1}"
                          .format(e, traceback.format_exc()))

            # Response parameters
            errorMessage = 'There was an issue on DialogFlow WebHook'

        return succeed
