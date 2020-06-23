from datetime import datetime
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.types import DateTime
from sqlalchemy.orm import relationship
from .db import Base

class User(Base):
    __tablename__="User"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    def __repr__(self):
        return '<User {}>'.format(self.username)


class TransAccount(Base):
    __tablename__='transaccount'
    account_id = Column('account_id',Integer,ForeignKey('Account.id'),primary_key=True)
    biztrans_id = Column('biztrans_id',Integer,ForeignKey('Biztrans.id'),primary_key=True)
    ammount = Column('ammount',Integer,nullable=False)
    account = relationship("Account",back_populates="biztransactions")
    biztrans = relationship("Biztrans",back_populates="accounts")

class Account(Base):
    __tablename__="Account"
    id = Column(Integer, primary_key=True,index=True)
    accountname= Column(String(140))
    accountnumber = Column(Integer,unique=True)
    biztransactions = relationship('TransAccount', back_populates='account')

class Biztrans(Base):
    __tablename__="Biztrans"
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime,default=datetime.utcnow)
    description = Column(String(140))
    accounts = relationship('TransAccount', back_populates='biztrans')

