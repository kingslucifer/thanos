# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:32:23 2018

@author: zy259
"""

from sqlalchemy import Column, Date, String, Float
from thanos.models import Base

class Top10WeeklyRecord(Base):
    __tablename__ = 'Top10WeeklyRecord'
    DATE = Column(Date, primary_key=True)
    NAME =  Column(String, primary_key=True)
    SYMBOL = Column(String)
    MARKET_CAP_USD = Column(Float)
    PERCENT_CHANGE_1H = Column(Float)
    PERCENT_CHANGE_24H = Column(Float)
    PERCENT_CHANGE_7D = Column(Float)
    PRICE_USD = Column(Float)
    INDEX_PORTION = Column(Float)

class Med40WeeklyRecord(Base):
    __tablename__ = 'Med40WeeklyRecord'
    DATE = Column(Date, primary_key=True)
    NAME =  Column(String, primary_key=True)
    SYMBOL = Column(String)
    MARKET_CAP_USD = Column(Float)
    PERCENT_CHANGE_1H = Column(Float)
    PERCENT_CHANGE_24H = Column(Float)
    PERCENT_CHANGE_7D = Column(Float)
    PRICE_USD = Column(Float)
    INDEX_PORTION = Column(Float)
    
class Small100WeeklyRecord(Base):
    __tablename__ = 'Small100WeeklyRecord'
    DATE = Column(Date, primary_key=True)
    NAME =  Column(String, primary_key=True)
    SYMBOL = Column(String)
    MARKET_CAP_USD = Column(Float)
    PERCENT_CHANGE_1H = Column(Float)
    PERCENT_CHANGE_24H = Column(Float)
    PERCENT_CHANGE_7D = Column(Float)
    PRICE_USD = Column(Float)
    INDEX_PORTION = Column(Float)

class Weekly_Factor(Base):
    __tablename__ = 'WeeklyFactor'
    DATE = Column(Date, primary_key=True)
    TOP10_FACTOR = Column(Float)
    MED40_FACTOR = Column(Float)
    SMALL100_FACTOR = Column(Float)

class Daily_Price(Base):
    __tablename__ = 'DailyPrice'
    DATE = Column(Date, primary_key=True)
    TOP10_PRICE = Column(Float)
    MED40_PRICE = Column(Float)
    SMALL100_PRICE= Column(Float)
