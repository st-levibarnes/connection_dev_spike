from odoo.tests.common import TransactionCase
from os import getenv
import pymssql

class TestConnection(TransactionCase):

    def test_connection_binding(self):
        "check if connection works"
        ConnectionBinding = self.env['connection_dev_spike.connection_binding']
        cb = ConnectionBinding.create({
            'name': 'mssql connection',
            'server': 'mssql',
            'userName': 'sa',
            'password': 'P@ssw0rd',
            'database': 'testdb'
        })
        self.assertEqual(cb.userName,"sa")
        with pymssql.connect(cb.server, cb.userName, cb.password, cb.database) as conn:
            cur = conn.cursor()
            testVal = 1
            cur.execute('SELECT * FROM test')
            self.assertEqual(cur.fetchone()[0],testVal)