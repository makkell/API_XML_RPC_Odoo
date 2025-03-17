import yaml
import xmlrpc.client

# Настройки подключения
url = "http://localhost:8069"
db = "mydb"
username = "admin"
password = "admin"

# Путь к YAML-файлу с данными
path_yaml_data_for_role = 'intern_base_role.yaml'

# Чтение данных из YAML-файла
with open(path_yaml_data_for_role, 'r') as file:
    data = yaml.safe_load(file)

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
    new_record_id = models.execute_kw(db, uid, password, 'res.users.role', 'create', [data])
    print(f"Record created successfully with ID: {new_record_id}")
except xmlrpc.client.Fault as e:
    print(f"Error creating record: {e.faultString}")