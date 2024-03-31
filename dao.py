import asyncio

from sqlalchemy import insert, select, update, delete


from models import User, Order
from database import async_session_maker

async def create_user(
        name: str,
        login: str,
        password: str,
        age: int,
        nickname: str = None,
        notes: str = None
) -> tuple:

    # await asyncio.sleep(2)
    # print(99999999)
    async with async_session_maker() as session:
        query = insert(User).values(
            name = name,
            login = login,
            password = password,
            age = age,
            nickname = nickname,
            notes = notes
        ).returning(User.id, User.created_at, User.login)
        print(query)
        data = await session.execute(query)
        await session.commit()
        print(tuple(data))
        return(tuple(data))[0]

async def fetch_users(skip: int = 0, limit: int = 10) -> list [User]:
    async with async_session_maker() as session:
        query = select(User).offset(skip).limit(limit)
        result = await session.execute(query)
        print(query)
        # print(type(result.scalars().all()))
        print(result.scalars().all()[0].created_at)
        return result.scalars().all()

async def get_user_by_id(user_id: int) -> User | None:
    async with async_session_maker() as session:
        query = select(User).filter_by(id=user_id)
        result = await session.execute(query)
        print(result.scalar_one_or_none())
        # return result.scalar_one_or_none()

async def update_user(user_id: int, values: dict):
    if not values: 
        return

    async with async_session_maker() as session:
        query = update(User).where(User.id == user_id).values(**values)
        result = await session.execute(query)
        await session.commit()
        # print(tuple(result))
        print(query)
        
async def delete_user(user_id: int):
    async with async_session_maker() as session:
        query = delete(User).where(User.id == user_id)
        await session.execute(query)
        await session.commit()
        print(query)


async def main():
    await asyncio.gather(
        # create_user(
        #     # name = 'Остап',
        #     # login = 'login8756746',
        #     # password = '1234',
        #     # age = 45,
        #     # nickname = 'nickName',
        # ),  # Добавляем запятую здесь
        # fetch_users(skip=0)
        # get_user_by_id(6)
        # update_user(4, {'name':'Alex','password' : '7898667986'})
        # delete_user(2)
    )

asyncio.run(main())
#---------------------------------------------------------------------

# async def create_order(quantity: int, price: float, customer_id: int) -> Order:
#     async with async_session_maker() as session:
#         query = insert(Order).values(
#             quantity=quantity,
#             price=price,
#             customer_id=customer_id
#         ).returning(Order)
#         result = await session.execute(query)
#         await session.commit()
#         return result.scalars().first()

# async def fetch_orders(skip: int = 0, limit: int = 10) -> list[Order]:
#     async with async_session_maker() as session:
#         query = select(Order).offset(skip).limit(limit)
#         result = await session.execute(query)
#         return result.scalars().all()

# async def get_order_by_id(order_id: int) -> Order | None:
#     async with async_session_maker() as session:
#         query = select(Order).filter_by(id=order_id)
#         result = await session.execute(query)
#         return result.scalar_one_or_none()

# async def update_order(order_id: int, values: dict):
#     if not values: 
#         return

#     async with async_session_maker() as session:
#         query = update(Order).where(Order.id == order_id).values(**values)
#         await session.execute(query)
#         await session.commit()

# async def delete_order(order_id: int):
#     async with async_session_maker() as session:
#         query = delete(Order).where(Order.id == order_id)
#         await session.execute(query)
#         await session.commit()

# async def main():
#     await asyncio.gather(
#         create_order(quantity=5, price=10.5, customer_id=2), 
#         # fetch_orders(),
#         # get_order_by_id(1),
#         # update_order(1, {'quantity': 10}),
#         # delete_order(1)
#     )

# asyncio.run(main())

async def create_order(quantity: int, price: float, customer_id: int) -> Order:
    async with async_session_maker() as session:
        query = insert(Order).values(
            quantity=quantity,
            price=price,
            customer_id=customer_id
        ).returning(Order)
        result = await session.execute(query)
        await session.commit()
        return result.scalars().first()

async def fetch_orders(skip: int = 0, limit: int = 10) -> list[Order]:
    async with async_session_maker() as session:
        query = select(Order).offset(skip).limit(limit)
        result = await session.execute(query)
        return result.scalars().all()

async def get_order_by_id(order_id: int) -> Order | None:
    async with async_session_maker() as session:
        query = select(Order).filter_by(id=order_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

async def update_order(order_id: int, values: dict):
    if not values:
        return

    async with async_session_maker() as session:
        query = update(Order).where(Order.id == order_id).values(**values)
        await session.execute(query)
        await session.commit()

async def delete_order(order_id: int):
    async with async_session_maker() as session:
        query = delete(Order).where(Order.id == order_id)
        await session.execute(query)
        await session.commit()

async def main():
    await asyncio.gather(
        create_order(quantity=6, price=45.67, customer_id=6),
        # fetch_orders(skip=0, limit=10),
        # get_order_by_id(order_id=1),
        # # update_order(order_id=1, values={'quantity': 20}),
        # delete_order(order_id=2)
    )

if __name__ == "__main__":
    asyncio.run(main())