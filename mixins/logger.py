from datetime import datetime

class logger:
    logs = {}
    nums = 1

    @classmethod
    def log(cls, message):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cls.logs[f'{cls.nums} {date}'] = message
        cls.nums += 1

    @classmethod
    def save_log(cls, filename):
        import json
        with open(f'logs/{filename}', 'w', encoding='utf-8') as file:
            json.dump(cls.logs, file, ensure_ascii=False, indent=4)
        pass


