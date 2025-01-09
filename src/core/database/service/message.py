from sqlalchemy import select

from src.core.database.models import User, Message
from src.core.database.context import DBContext


class MessageService(DBContext):
    async def add_message_by_user_id(
            self,
            user_id: int,
            message: Message
    ) -> Message | None:
        async with self.session() as session:
            stmt = (
                select(User)
                .where(User.user_id == user_id)
            )
            user = await session.execute(stmt)
            user = user.scalars_one_or_none()
            if not user:
                raise ValueError(f"User with user_id={user_id}")
            user.messages.append(message)
            session.add(user)
            await session.commit()
            return message
