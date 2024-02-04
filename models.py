from typing import Optional
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from database import Base
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    login: Mapped[str] = mapped_column(String(30), unique = True, index = True )
    password: Mapped[str] 
    nickname: Mapped[Optional[str]]
    is_active: Mapped[bool] = mapped_column(default = True)

def __repr__(self) -> str:
    return f'User {self.name} #{self.id}'

# from datetime import datetime
# from typing import Optional

# from sqlalchemy import ForeignKey
# from sqlalchemy import func
# from sqlalchemy import Integer
# from sqlalchemy import String
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import registry
# from sqlalchemy.orm import relationship

# mapper_registry = registry()


# @mapper_registry.mapped
# class User:
#     __tablename__ = "users"

#     id = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] 
#     login: Mapped[str] = mapped_column(String(30), unique = True, index = True )
#     password: Mapped[str]
#     nickname: Mapped[Optional[str]]
#     is_active: Mapped[bool] = mapped_column(default = True)



# # @mapper_registry.mapped
# # class Address:
# #     __tablename__ = "address"

# #     id = mapped_column(Integer, primary_key=True)
# #     user_id = mapped_column(ForeignKey("user.id"))
# #     email_address: Mapped[str]

# #     user: Mapped["User"] = relationship(back_populates="addresses")
