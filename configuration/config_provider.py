import configparser

class ConfigProvider:
    def __init__(self, filename: str) -> None:
        self.config = configparser.ConfigParser()
        self.config.read(filename)  # Не присваивайте результат read() никуда

    def get(self, section: str, key: str):
        return self.config[section][key]  # Используйте self.config

    def get_int(self, section: str, key: str):
        return self.config[section].getint(key)
    
    def get_db_connection_string(self):
        return self.get("database", "connection_string")