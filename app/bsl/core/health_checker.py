from sqlalchemy import text
from redis import Redis

from bsl.core import database, settings


class HealthCheck:
    def __init__(self, name: str):
        self.name = name

    async def check(self):
        raise NotImplementedError


class RedisChecker(HealthCheck):
    def __init__(self, name="RedisChecker"):
        super().__init__(name)

    async def check(self):
        status = False

        try:
            redis = Redis(host=settings.REDIS_HOST, password=settings.REDIS_PASSWORD)
            test_key = 'health_check_test'
            redis.set(test_key, 'value')
            result = redis.get(test_key)

            redis.delete(test_key)
            status = True

            redis.close()
        except Exception as e:
            print("RedisChecker:", e)

        return status


class DatabaseChecker(HealthCheck):
    def __init__(self, name="DatabaseChecker"):
        super().__init__(name)

    async def check(self):
        status = False

        is_connected = database.is_connected

        try:
            if not is_connected:
                await database.connect()

            query = text("select 1")

            result = await database.fetch_one(query)

            if not is_connected:
                await database.disconnect()
            status = True
        except Exception as e:
            print("DatabaseChecker:", e)

        return status
