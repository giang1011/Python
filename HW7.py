import asyncio

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

async def main():
    a, b = 10, 5

    result_add = await asyncio.to_thread(add, a, b)
    result_subtract = await asyncio.to_thread(subtract, a, b)
    result_multiply = await asyncio.to_thread(multiply, a, b)   
    result_divide = await asyncio.to_thread(divide, a, b)

    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_subtract}")
    print(f"{a} * {b} = {result_multiply}")
    print(f"{a} / {b} = {result_divide}")

asyncio.run(main())