# Questo modulo utilizza Flask per realizzare un web server. L'applicazione può essere eseguita in vari modi
# FLASK_APP=server.py FLASK_ENV=development flask run #LINUX
# set FLASK_APP=server.py 
# set FLASK_ENV=development 
# flask run #WINDOWS
# python server.py

from flask import Flask, request
import user

# viene creata l'applicazione con il nome del modulo corrente.
app = Flask(__name__)

# getErrorCode è una funzione di utilità che mappa i valori ritornati dal modulo database con quelli del
# protocollo HTTP in caso di errore. 
# 404 - Not Found: una risorsa non è stata trovata sul server;
# 403 - Forbidden: accesso negato;
# 409 - Conflict: è violato un vincolo di unicità. Ad esempio, esiste già un utente con la stessa mail registrata;
# Come ultima spiaggia è buona norma ritornare "500 - Internal Server Error" per indicare che qualcosa è andato storto
def getErrorCode(result: user.Result)->int:
    
    if result is user.Result.NOT_FOUND:
        code = 404
    elif result is user.Result.NOT_AUTHORIZED:
        code = 403
    elif result is user.Result.DUPLICATED:
        code = 409
    else:
        code = 500

    return code

@app.route('/user', methods=['POST'])
def createUser():
    data = request.get_json()
    name = data['name']
    surname = data['surname']
    email = data['email']
    password = data['password']
    
    result, u = user.SaveUser(name, surname, email, password)

    if result is not user.Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        return u, 201


if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)
