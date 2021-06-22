import databases
import sqlalchemy
import psycopg2

from bsl.core.config import settings

database = databases.Database(settings.SQLALCHEMY_DATABASE_URI)

metadata = sqlalchemy.MetaData()


class PsqlManager:
    def __init__(self, host, database, user, password):
        self.is_connection = False
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password)
        self.is_connection = True

    def execute(self, query):
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        cur.close()

    def fetch_all(self, query):
        cur = self.connection.cursor()
        cur.execute(query)
        response = cur.fetchall()
        self.connection.commit()
        cur.close()
        return response


psql_manager = PsqlManager(
    settings.POSTGRES_SERVER, settings.POSTGRES_DB, settings.POSTGRES_USER, settings.POSTGRES_PASSWORD
)
