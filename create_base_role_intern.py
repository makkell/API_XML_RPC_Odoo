import json
import xmlrpc.client

url = "http://localhost:8069" # твой url
db = "mydb" # твоя бд
username = "admin"
password = "admin"
TOKEN = "2e2d522c71443b69cf13880aa246eacaa493ea6c" #токен  (необязательно)

path_json_data_for_role = 'intern.json'

with open('intern.json', 'r') as file:
    data = json.load(file)


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

models.execute_kw(db, uid, password, 'res.users.role', 'create', [data]) # создание роли 