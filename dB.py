import sqlite3
from datetime import date
import json
from typing import Optional, Dict


class SimpleUserDB:
    def __init__(self, db_path: str = "users.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                uid INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                day_streak INTEGER DEFAULT 0,
                last_date TEXT,
                history TEXT DEFAULT '{}',
                history_dates TEXT DEFAULT '{}'
            )
        """)
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()

    # ────────────────────────────────
    # Создание пользователя
    # ────────────────────────────────

    def create_user(self, username: str, password: str) -> int:
        """Возвращает uid нового пользователя или поднимает исключение"""
        try:
            self.cursor.execute(
                "INSERT INTO users (username, password, last_date) VALUES (?, ?, ?)",
                (username, password, date.today().isoformat())
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"Username '{username}' уже занят")

    # ────────────────────────────────
    # Поиск uid по username (новый метод)
    # ────────────────────────────────

    def get_uid_by_username(self, username: str) -> Optional[int]:
        """Возвращает uid пользователя по его имени или None, если такого нет"""
        self.cursor.execute(
            "SELECT uid FROM users WHERE username = ?",
            (username,)
        )
        row = self.cursor.fetchone()
        return row["uid"] if row else None

    # ────────────────────────────────
    # Получение значений (по uid)
    # ────────────────────────────────

    def get_username(self, uid: int) -> Optional[str]:
        row = self._get_row(uid)
        return row["username"] if row else None

    def get_password(self, uid: int) -> Optional[str]:
        row = self._get_row(uid)
        return row["password"] if row else None

    def get_day_streak(self, uid: int) -> Optional[int]:
        row = self._get_row(uid)
        return row["day_streak"] if row else None

    def get_last_date(self, uid: int) -> Optional[str]:
        row = self._get_row(uid)
        return row["last_date"] if row else None

    def get_history(self, uid: int) -> Dict:
        row = self._get_row(uid)
        if not row:
            return {}
        try:
            return json.loads(row["history"])
        except (json.JSONDecodeError, TypeError):
            return {}
    
    def get_history_dates(self, uid: int) -> Dict:
            row = self._get_row(uid)
            if not row:
                return {}
            try:
                return json.loads(row["history_dates"])
            except (json.JSONDecodeError, TypeError):
                return {}

    def get_all_data(self, uid: int) -> Optional[dict]:
        row = self._get_row(uid)
        if not row:
            return None
        data = dict(row)
        try:
            data["history"] = json.loads(data["history"])
        except Exception:
            data["history"] = {}
        return data

    def _get_row(self, uid: int) -> Optional[sqlite3.Row]:
        self.cursor.execute("SELECT * FROM users WHERE uid = ?", (uid,))
        return self.cursor.fetchone()

    # ────────────────────────────────
    # Запись значений (по uid)
    # ────────────────────────────────

    def set_password(self, uid: int, new_password: str) -> bool:
        self.cursor.execute(
            "UPDATE users SET password = ? WHERE uid = ?",
            (new_password, uid)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def set_day_streak(self, uid: int, value: int) -> bool:
        self.cursor.execute(
            "UPDATE users SET day_streak = ? WHERE uid = ?",
            (value, uid)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def set_last_date(self, uid: int, value: str | date) -> bool:
        if isinstance(value, date):
            value = value.isoformat()
        self.cursor.execute(
            "UPDATE users SET last_date = ? WHERE uid = ?",
            (value, uid)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def set_history(self, uid: int, history_dict: dict) -> bool:
        json_str = json.dumps(history_dict, ensure_ascii=False)
        self.cursor.execute(
            "UPDATE users SET history = ? WHERE uid = ?",
            (json_str, uid)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def set_history_dates(self, uid: int, history_dict: dict) -> bool:
        json_str = json.dumps(history_dict, ensure_ascii=False)
        self.cursor.execute(
            "UPDATE users SET history_dates = ? WHERE uid = ?",
            (json_str, uid)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def update_streak_and_date(self, uid: int, streak: int, last_date: str | date) -> bool:
        if isinstance(last_date, date):
            last_date = last_date.isoformat()
        self.cursor.execute(
            "UPDATE users SET day_streak = ?, last_date = ? WHERE uid = ?",
            (streak, last_date, uid)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0


# Пример использования нового метода
if __name__ == "__main__":
    db = SimpleUserDB("users.db")

    # Создаём тестового пользователя (если ещё нет)
    try:
        uid = db.create_user("ivan", "qwerty123")
        print(f"Создан пользователь ivan → uid = {uid}")
    except ValueError:
        pass

    # Получаем uid по имени
    found_uid = db.get_uid_by_username("ivan")
    print(f"uid для ivan: {found_uid}")

    if found_uid:
        print("Стрик:", db.get_day_streak(found_uid))
        db.set_day_streak(found_uid, 5)
        print("Новый стрик:", db.get_day_streak(found_uid))

    db.close()