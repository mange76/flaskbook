#!/usr/bin/python3

from app import models
from app.db import SessionLocal,engine

db = SessionLocal()
models.Base.metadata.create_all(bind=engine)

account_record = models.Account(accountname='Transaktionskonto Bank',accountnumber=1910)
db.add(account_record)
account_record = models.Account(accountname='Utgående MOMS 25%',accountnumber=2611)
db.add(account_record)
account_record = models.Account(accountname='Debiterad ingående MOMS',accountnumber=2641)
db.add(account_record)
account_record = models.Account(accountname='Försäljning datorer',accountnumber=3010)
db.add(account_record)
account_record = models.Account(accountname='inköp komponenter',accountnumber=4010)
db.add(account_record)
db.commit()

account_record=db.query(models.Account).filter_by(accountnumber=1910).all()

db.close()

