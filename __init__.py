# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'GoogleDocs' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

import pickle
import os.path
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

global read_elements


def read_elements(elements):
    text = ''
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for element in elements:
                text_run = element.get('textRun')
                if not text_run:
                    text += ''
                else:
                    text += text_run.get('content')
        elif 'table' in value:
            table = value.get('table')
            for row in table.get('tableRows'):
                for cell in row.get('tableCells'):
                    text += read_elements(cell.get('content'))
        elif 'tableOfContents' in value:
            toc = value.get('tableOfContents')
            text += read_elements(toc.get('content'))
    return text


module = GetParams("module")

global creds
global document_id

if module == "GoogleSuite":
    credential_path = GetParams("credentials")
    print(credential_path)
    if not os.path.exists(credential_path):
        raise Exception("El archivo de credenciales no existe en la ruta especificada")

    SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive']

    creds = None

    if os.path.exists('token-docs.pickle'):
        with open('token-docs.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credential_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token-docs.pickle', 'wb') as token:
            pickle.dump(creds, token)

if module == "new_docs":
    title = GetParams("doc_name")
    result = GetParams("result")

    body = {
        'title': title
    }
    service = build('docs', 'v1', credentials=creds)
    request = service.documents().create(body=body)
    response = request.execute()
    document_id = response["documentId"]
    if result:
        SetVar(result, document_id)
    print(response)

if module == "write":
    doc_id = GetParams("doc_id")
    text = GetParams("text")

    texto = text.split("\\n ")

    text = ""
    for line in texto:
        text += "\n" + line

    service = build('docs', 'v1', credentials=creds)
    content = service.documents().get(documentId=doc_id).execute().get('body').get('content')

    for element in content:
        index = element.get("endIndex")

    body = {
        "requests": [
            {
                "insertText": {
                    "text": text,
                    "location": {
                        "index": index - 1
                    }
                }
            },
            {
                "deleteParagraphBullets": {
                    "range": {
                        "startIndex": index,
                        "endIndex": index + len(text)
                    }
                }
            }
        ]
    }
    response = service.documents().batchUpdate(documentId=doc_id, body=body).execute()


if module == "read":

    doc_id = GetParams("doc_id")
    result = GetParams("result")

    service = build('docs', 'v1', credentials=creds)

    request = service.documents().get(documentId=doc_id)
    response = request.execute()

    content = response.get('body').get('content')

    if result:
        SetVar(result, read_elements(content))

if module == "add_pic":

    doc_id = GetParams("doc_id")
    img = GetParams("img_path")


    service = build('docs', 'v1', credentials=creds)
    content = service.documents().get(documentId=doc_id).execute().get('body').get('content')

    for element in content:
        index = element.get("endIndex")

    body = {
        "requests": [
            {
                "insertText": {
                    "text": "\n",
                    "location": {
                        "index": index - 1
                    }
                }
            },
            {
                "insertInlineImage": {
                    "uri": img,
                    "location": {
                        "index": index
                    }
                }
            }
        ]
    }
    response = service.documents().batchUpdate(documentId=doc_id, body=body).execute()
