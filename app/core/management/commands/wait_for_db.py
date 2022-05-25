"""
django command to wait for database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django command to wait for database"""

    def handle(self,*arg,**options):
        """ Entrypoint for command """
        self.stdout.write('waiting for database...')
        db_up =  False
        while db_up is False:
            # import pdb; pdb.set_trace()
            try:
                self.check(databases=['default'])
                
                db_up = True
            except (Psycopg2OpError,OperationalError):
                
                self.stdout.write('database unavailable, waiting for 1sec...')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database available'))