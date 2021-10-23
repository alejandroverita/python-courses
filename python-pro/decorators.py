from datetime import datetime

# Recibe una funcion como parametro: Closure
def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Han transcurrido {time_elapsed.total_seconds()} segundos")

    return wrapper


# decorador
@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass


@execution_time
def sum(a: int, b: int) -> int:
    return a + b


sum(5, 5)
random_func()
