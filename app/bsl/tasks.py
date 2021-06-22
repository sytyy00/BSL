from huey import crontab

from bsl.main import huey
from bsl.core import psql_manager


@huey.periodic_task(crontab(minute='*/10'))
def update_holds():
        rows = psql_manager.fetch_all("""
        SELECT users.uuid, users.name, users.balance, users.holds, users.status 
        FROM users 
        WHERE users.holds != 0
        """)
        for row in rows:

            query = f"""
            UPDATE users SET holds = 0, balance = {row[2] - row[3]} WHERE uuid = \'{row[0]}\'
            """
            psql_manager.execute(query)


