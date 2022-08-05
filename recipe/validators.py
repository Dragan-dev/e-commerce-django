import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError



valid_unit_value=['grams', 'litre', 'pounds', 'packs']
# clear_values=", ".join(valid_unit_value)

def validate_unit_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_values = ureg[value]
    except UndefinedUnitError as e:
                raise ValidationError(f"'{value}' is not valid unit") 
    except :
        raise ValidationError(f"{value} is invalid value") 



