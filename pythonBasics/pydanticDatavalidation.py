from pydantic import BaseModel, ValidationError
from typing import Any

class StaticModel(BaseModel):
    a: int
    b: int

    def add_numbers(self)-> int:
        return self.a+ self.b
    

class DynamicModel(BaseModel):
    a:object
    b:object

    def add_numbers(self):
        return self.a +self.b
    


if __name__=='__main__':
    try:
        static_instance= StaticModel(a=10, b=20)
        result_static= static_instance.add_numbers()
        print(f"Static Typing Result: {result_static}")
    except ValidationError as e:
        print(f"Static Typing Validation Error: {e}")

    
    # Dynamic Typing Example
    dynamic_instance = DynamicModel(a=10, b=20)
    result_dynamic = dynamic_instance.add_numbers()
    print(f"Dynamic Typing Result (int + int): {result_dynamic}")

    dynamic_instance_str = DynamicModel(a="hello", b="world")
    result_dynamic_str = dynamic_instance_str.add_numbers()
    print(f"Dynamic Typing Result (str + str): {result_dynamic_str}")

    # The following will cause a runtime error since you can't add int and str
    dynamic_instance_error = DynamicModel(a=10, b="world")
    result_dynamic_error = dynamic_instance_error.add_numbers()
    print(f"Dynamic Typing Result (int + str): {result_dynamic_error}")

