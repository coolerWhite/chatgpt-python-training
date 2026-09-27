#!/usr/bin/python
# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


# Модуль должен:

# Принимать обязательный строковый параметр path.
# Проверять, что путь указывает на обычный файл.
# Возвращать changed: false, path (переданную строку) и size_bytes (целое число — размер в байтах).
# Для отсутствующего файла, директории или ошибки доступа завершаться через fail_json с понятным msg. Точный текст сообщения любой.
# Работать с --check и возвращать те же данные: он только собирает информацию.

from ansible.module_utils.basic import AnsibleModule
from pathlib import Path


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    file_name = module.params["path"]
    try:
        result = inspect_file(file_name)
    except (ValueError, OSError) as error:
        module.fail_json(msg=str(error))

    module.exit_json(changed=False, **result)


def inspect_file(file_name):
    file_path = Path(file_name)

    if not file_path.is_file():
        raise ValueError(f"{file_path} is not File")

    file_size = file_path.stat().st_size

    return {
        "path": file_name,
        "size_bytes": file_size
    }


def main():
    run_module()
if __name__ == "__main__":
    main()
# ПСЕВДОКОД ДЛЯ ТОЧКИ ВХОДА:
# 1. Создать функцию main(), которая вызывает run_module().
# 2. В конце файла проверить, что модуль запущен напрямую.
# 3. Если да — вызвать main().
