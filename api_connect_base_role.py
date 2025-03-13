url = "http://localhost:8069" 
db = "mydb"
username = "admin"
password = "admin"
TOKEN = "2e2d522c71443b69cf13880aa246eacaa493ea6c"


"""
Я тут функционал щупаю и забираю данные 
"""


import xmlrpc.client
import json

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

ids = models.execute_kw(db, uid, password, 'res.users.role', 'search', [[['name', '=', 'Стажер (склад+продажи)']]], {'limit': 1})

[record] = models.execute_kw(db, uid, password, 'res.users.role', 'read', [ids])

print(record)

model_access_ids = record['model_access_ids']
implied_ids = record['implied_ids']
trans_implied_ids = record['trans_implied_ids']

data = {
    'model_access_ids': model_access_ids, 
    'name' : "Стажёр", 
    'implied_ids': implied_ids,
    'trans_implied_ids': trans_implied_ids
}
with open('intern_base_role.json', 'w') as file:
    json.dump(data, file)

help_model = models.execute_kw(db, uid, password, 'res.users.role', 'fields_get', [], {'attributes': ['string', 'help', 'type']}) # Список полей модели

# for key, value in help_model.items():
#     print(f"{key} : {value}")

models.execute_kw(db, uid, password, 'res.users.role', 'create', [data]) # создание записи в модели  'model_access_ids': model_access_ids
# ids = models.execute_kw(db, uid, password, 'res.users.role', 'search', [[['name', '=', 'name']]], {'limit': 1})
# models.execute_kw(db, uid, password, 'res.users.role', 'write', [[ids[0]], data ])

# print(help_model)
