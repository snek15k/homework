import datetime
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования выполнения функции.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.datetime.now()
            log_message = f"{start_time} - Начало выполнения функции '{func.__name__}'.\n"

            try:
                result = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                log_message += (
                    f"{end_time} - Успешное завершение функции '{func.__name__}' "
                    f"с результатом: {result}.\n"
                )
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_time = datetime.datetime.now()
                log_message += (
                    f"{error_time} - Ошибка в функции '{func.__name__}': {type(e).__name__} - {e}. "
                    f"Аргументы: {args}, {kwargs}.\n"
                )
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                raise
        return wrapper
    return decorator
