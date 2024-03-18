# Django가 DB 연결에 실패했을 시, 재시도하도록 하는 로직을 추가

from django.db import connections
from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Wating for DB Connections...")

        is_db_connected = None

        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except :
                self.stdout.write("Connection Trying ...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('PostgreSQL Connections Success'))