import json
import xmlrpc.client

# Настройки подключения
url = "http://localhost:8069"  # URL сервера Odoo
db = "mydb"  # Имя базы данных
username = "admin"  # Логин пользователя
password = "admin"  # Пароль пользователя

# Путь к JSON-файлу с данными
path_json_data_for_role = 'intern_base_role.json'

# Чтение данных из JSON-файла
with open('intern_sale_access_studio.json', 'r') as file:
    data = json.load(file)

# Подключение к серверу
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("Odoo version:", common.version())

# Аутентификация
uid = common.authenticate(db, username, password, {})
if not uid:
    raise Exception("Authentication failed")

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Создание записи
try:
    print("Creating record with data:", data)
    new_record_id = models.execute_kw(db, uid, password, 'access.management', 'create', [data])
    print(f"Record created successfully with ID: {new_record_id}")
except xmlrpc.client.Fault as e:
    print(f"Error creating record: {e.faultString}")