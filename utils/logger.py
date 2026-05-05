import logging
import sys
from pathlib import Path


def setup_logger(name: str = __name__, log_level: str = "INFO") -> logging.Logger:
    """
    Настройка логгера с выводом в консоль и файл.
    
    Args:
        name: Имя логгера (обычно __name__)
        log_level: Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    
    Returns:
        Настроенный объект логгера
    """
    logger = logging.getLogger(name)
    
    if logger.handlers:
        # Логгер уже настроен
        return logger
    
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    # Форматтер
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Обработчик для консоли
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Обработчик для файла
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(log_dir / "test_execution.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger