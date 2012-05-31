
import sys
from  sqlalchemy import *

db = create_engine('oracle://OTTO:db4auto@crouton.stanford.edu:1521/SGD')

metadata = MetaData(db)
feature = Table('feature',metadata,autoload=True,schema='bud')

smt = select(feature.c.feature_type == 'ORF')
orfs = db.execute(smt)
print orfs.rowcount
print orfs.first()

