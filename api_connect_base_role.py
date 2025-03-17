import yaml
import xmlrpc.client

# Настройки подключения
url = "http://localhost:8069"
db = "mydb"
username = "admin"
password = "admin"

# Подключение к серверу
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("Odoo version:", common.version())

# Аутентификация
uid = common.authenticate(db, username, password, {})
if not uid:
    raise Exception("Authentication failed")

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Поиск записи роли по имени
ids = models.execute_kw(db, uid, password, 'res.users.role', 'search', [[['name', '=', 'Стажер (склад+продажи)']]], {'limit': 1})


# Чтение данных записи
[record] = models.execute_kw(db, uid, password, 'res.users.role', 'read', [ids])
print("Record data:", record)

# Формирование данных для YAML-файла
data = {
    'name': record['name'],  # Добавляем название роли
    'model_access_ids': record['model_access_ids'],
    'implied_ids': record['implied_ids'],
    'trans_implied_ids': record['trans_implied_ids']
}

# Сохранение данных в YAML-файл
with open('intern_base_role.yaml', 'w') as file:
    yaml.dump(data, file, allow_unicode=True, sort_keys=False)
print("Data saved to YAML file")