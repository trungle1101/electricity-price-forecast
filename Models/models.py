from email.utils import make_msgid
from os import name
from typing import no_type_check
from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Boolean, func, FetchedValue
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, JSON
from sqlalchemy.schema import UniqueConstraint


Base = declarative_base()
Session = sessionmaker()