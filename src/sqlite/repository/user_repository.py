from src.sqlite.db.database import get_connection
from src.sqlite.models.user import User
from src.sqlite.interfaces.i_user_repository import IUserRepository

class UserRepository(IUserRepository):

    def get_all_users(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()

        conn.close()

        return [User(*row) for row in rows]

    def create_user(self, name, email):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )

        conn.commit()
        conn.close()