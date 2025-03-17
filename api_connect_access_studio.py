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

# Поиск записи
ids = models.execute_kw(db, uid, password, 'access.management', 'search', [[['name', '=', 'Стажер (продажи)']]])

print("Found record IDs:", ids)

# Чтение данных записи
[record] = models.execute_kw(db, uid, password, 'access.management', 'read', [ids])
print("Record data:", record)

# Формирование данных для обновления
data = {
    'name': record['name'],  # Добавляем название роли
    'hide_menu_ids': record['hide_menu_ids'],
    'hide_field_ids': record['hide_field_ids'],
    'remove_action_ids': record['remove_action_ids'],
    'access_domain_ah_ids': record['access_domain_ah_ids'],
    'hide_view_nodes_ids': record['hide_view_nodes_ids'],
    'self_module_menu_ids': record['self_module_menu_ids'],
    'hide_chatter_ids': record['hide_chatter_ids'],
    'hide_chatter': record['hide_chatter'],
    'hide_send_mail': record['hide_send_mail'],
    'hide_log_notes': record['hide_log_notes'],
    'hide_schedule_activity': record['hide_schedule_activity'],
    'hide_export': record['hide_export'],
    'hide_import': record['hide_import'],
    'hide_spreadsheet': record['hide_spreadsheet'],
    'hide_add_property': record['hide_add_property'],
    'disable_login': record['disable_login'],
    'disable_debug_mode': record['disable_debug_mode'],
    'hide_filters_groups_ids': record['hide_filters_groups_ids'],
    'is_apply_on_without_company': record['is_apply_on_without_company']
}

# Сохранение данных в YAML-файл
with open('intern_sale_access_studio.yaml', 'w') as file:
    yaml.dump(data, file, allow_unicode=True, sort_keys=False)
print("Data saved to YAML file")

# # Обновление записи
# try:
#     print("Updating record with data:", data)
#     models.execute_kw(db, uid, password, 'access.management', 'write', [[ids[0]], data])
#     print("Record updated successfully")
# except xmlrpc.client.Fault as e:
#     print(f"Error updating record: {e.faultString}")