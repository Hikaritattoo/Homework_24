from dataclasses import dataclass
from typing import Union

import marshmallow_dataclass
from marshmallow import ValidationError

from projectdata.config import COMMANDS


@dataclass
class Commands:
    file_name: str
    cmd1: str
    value1: Union[str, int]
    cmd2: str
    value2: Union[str, int]

    def __post_init__(self):
        """Проверяет поля и объединяет команды с '_'"""
        if self.cmd1 not in COMMANDS:
            raise ValidationError(f'Команда cmd1 ({self.cmd1}) некорректна. '
                                  f'Необходимо ввести {", ".join(COMMANDS)}')
        if self.cmd2 not in COMMANDS:
            raise ValidationError(f'Команда cmd2 ({self.cmd2}) некорректна. '
                                  f'Необходимо ввести {", ".join(COMMANDS)}')

        self.cmd1 = self.cmd1 + '_'
        self.cmd2 = self.cmd2 + '_'


CommandsSchema = marshmallow_dataclass.class_schema(Commands)
