# -*- coding: utf-8 -*-
import json

dict_text = {
    "list_stair": [],
    "delete_from_right_stoyak": []
}

# создаем файл json
with open('user_define.json', 'w') as file:
    json.dump(dict_text, file, indent=4)
