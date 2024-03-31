from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# from sqlalchemy import DateTime
# from sqlalchemy import Column
# from database import Base
# from datetime import datetime

# class BaseInfoMixin:
#     id: int = Column(Integer, primary_key=True)
#     created_at: datetime = Column(DateTime, default=datetime.utcnow)
#     notes: str = Column(String)

# class Address(BaseInfoMixin, Base):
#     __tablename__ = "addresses"

#     country: str = Column(String, nullable=False)

#     user_id: int = Column(Integer, ForeignKey('users.id'))
#     street: str = Column(String, default="І.Франка")
#     index: str = Column(String(5), Boolean=True)  # исправлено Boolean

#     user = relationship("User", back_populates="addresses")

# class User(BaseInfoMixin, Base):
#     __tablename__ = "users"

#     name: str = Column(String)
#     login: str = Column(String(30), unique=True, index=True)
#     password: str = Column(String)
#     nickname: str = Column(String, Boolean=True)  # исправлено Boolean
#     is_active: bool = Column(Boolean, default=True)
#     age: int = Column(Integer)
#     money: int = Column(Integer, default=0)

#     orders = relationship('Order', back_populates='user')
#     addresses = relationship("Address", back_populates="user")

#     def __repr__(self) -> str:
#         return f'User {self.name} #{self.id}'

# class Order(BaseInfoMixin, Base):
#     __tablename__ = 'orders'  # исправлено 'orders'
#     quantity: int = Column(Integer)
#     price: float = Column(Float)
#     customer: int = Column(Integer, ForeignKey('users.id'))

#     user = relationship('User', back_populates='orders')

from sqlalchemy import DateTime, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class BaseInfoMixin:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    notes: Mapped[Optional[str]]

class Address(BaseInfoMixin, Base):
    __tablename__ = "addresses"

    country = Column(String, nullable=False)
    region = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    street = Column(String, default="І.Франка")
    index = Column(String(5))  # Исправлено

    user = relationship("User", back_populates="addresses")

class User(BaseInfoMixin, Base):
    __tablename__ = "users"

    name = Column(String)
    login = Column(String(30), unique=True, index=True)
    password = Column(String)
#    nickname = Column(String)  # Исправлено
    nickname: Mapped[Optional[str]]  # Исправлено

    is_active: Mapped[bool] = mapped_column(default=True)
    age = Column(Integer)
    money = Column(Integer, default=0)

    orders = relationship('Order', back_populates='user')
    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f'User {self.name} #{self.id}'

# class Order(BaseInfoMixin, Base):
#     __tablename__ = 'orders'  
#     quantity = Column(Integer)
#     price = Column(Float)
#     customer = Column(Integer, ForeignKey('users.id'))

#     user = relationship('User', back_populates='orders')

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    quantity = Column(Integer)
    price = Column(Float)
    customer_id = Column(Integer, ForeignKey('users.id'))  # ForeignKey на идентификатор пользователя

    # Добавляем отношение с классом User
    user = relationship('User', back_populates='orders') 