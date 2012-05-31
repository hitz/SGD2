#! /usr/bin/env ptyhon

import cx_Oracle
host = 'crouton.stanford.edu'
port = 1521
SID = 'SGD'
dsn_tns = cx_Oracle.makedsn(host, port, SID)

db = cx_Oracle.connect('OTTO', 'db4auto', dsn_tns)
c = db.cursor()
c.execute("select count(*) from bud.feature")
print c.description
print [ row for row in c]

