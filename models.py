from typing import Optional
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from database import Base
#------------------------------------------------------------------------
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

# class Address(Base):
#     __tablename__ = "addresses"

#     id = Column(Integer, primary_key=True)
#     country = Column(String, nullable=False)

#     street = Column(String, default="вулиця І.Франка")
#     user_id = Column(Integer, ForeignKey('users.id'))
#     index = Column(String(5), nullable=True) #стрічка index довжиною 5 символів

#     # Добавляем отношение с таблицей пользователей
#     user = relationship("User", back_populates="addresses")

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     login = Column(String(30), unique=True, index=True)
#     password = Column(String)
#     nickname = Column(String, nullable=True)
#     is_active = Column(Boolean, default=True)

#     addresses = relationship("Address", back_populates="user")

#     def __repr__(self):
#         return f'User {self.name} #{self.id}'

#------------------------------------------------------------------------
# class Address(Base):
#     __tablename__ = "addresses"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     country: Mapped[str] = mapped_column(nullable=False)
#     user_id: Mapped[int](ForeignKey('users.id'))
#     index: Mapped[Optional[str]] = mapped_column(String(5))#стрічка індекс довжиною 5 символів

#     # Добавляем отношение с таблицей пользователей
#     user = relationship("User", back_populates="addresses")

# from database import Base
# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     login: Mapped[str] = mapped_column(String(30), unique = True, index = True )
#     password: Mapped[str] 
#     nickname: Mapped[Optional[str]]
#     is_active: Mapped[bool] = mapped_column(default = True)


#     def __repr__(self) -> str:
#         return f'User {self.name} #{self.id}'




#------------------------------------------------------------------------

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Address(Base):
    __tablename__ = "addresses"

    id: int = Column(Integer, primary_key=True)
    country: str = Column(String, nullable=False)
    region: str = Column(String, nullable=False)
    user_id: int = Column(Integer, ForeignKey('users.id'))
    street: str = Column(String, default="І.Франка")
    index: Optional[str] = Column(String(5))  # Строка индекса длиной 5 символов

    # Добавляем отношение с таблицей пользователей
    user = relationship("User", back_populates="addresses")

class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    login: str = Column(String(30), unique=True, index=True)
    password: str = Column(String) 
    nickname: Optional[str] = Column(String)
    is_active: bool = Column(Boolean, default=True)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self) -> str:
        return f'User {self.name} #{self.id}'
