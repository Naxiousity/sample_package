# sample_package/module.py

class Greeter:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}!"

def add(a: int, b: int) -> int:
    return a + b
