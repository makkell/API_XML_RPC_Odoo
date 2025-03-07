import json
import xmlrpc.client

url = "http://localhost:8069" # твой url
db = "mydb" # твоя бд
username = "admin"
password = "admin"
TOKEN = "2e2d522c71443b69cf13880aa246eacaa493ea6c" #токен  (необязательно)

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

print(common.version())

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


ids = models.execute_kw(db, uid, password, 'access.management', 'search', [[['name', '=', 'Тест api']]])

[record] = models.execute_kw(db, uid, password, 'access.management', 'read', [ids])

name = "Тест api"
data = {
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

with open('intern_sale_access_studio.json', 'w') as file:
    json.dump(data, file)

print(record)

models.execute_kw(db, uid, password, 'access.management', 'write', [[ids[0]], data ]) # создание роли 