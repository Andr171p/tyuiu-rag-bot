from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from src.db.database_manager import DatabaseManager
    
from sqlalchemy import select, func
    
from src.db.crud.base_crud import BaseCRUD
from src.db.models import DialogModel


class DialogCRUD(BaseCRUD):
    def __init__(self, manager: "DatabaseManager") -> None:
        self._manager = manager
        
    async def create(self, dialog: DialogModel) -> int:
        async with self._manager.session() as session:
            session.add(dialog)
            id = dialog.id
            await session.commit()
        return id
    
    async def read_by_user_id(self, user_id: int) -> Sequence[DialogModel] | None:
        async with self._manager.session() as session:
            stmt = (
                select(DialogModel)
                .where(DialogModel.user_id == user_id)
            )
            dialogs = await session.execute(stmt)
        return dialogs.scalars().all()
    
    async def read_by_user_id_with_limit(
        self,
        user_id: int,
        page: int = 1,
        limit: int = 5
    ) -> Sequence[DialogModel] | None:
        offset = (page - 1) * limit
        async with self._manager.session() as session:
            stmt = (
                select(DialogModel)
                .where(DialogModel.user_id == user_id)
                .offset(offset)
                .limit(limit)   
            )
            dialogs = await session.execute(stmt)
        return dialogs.scalars().all()
    
    async def read_all(self) -> Sequence[DialogModel] | None:
        async with self._manager.session() as session:
            stmt = select(DialogModel)
            dialogs = await session.execute(stmt)
        return dialogs.scalars().all()
    
    async def read_count_by_user_id(self, user_id: int) -> int | None:
        async with self._manager.session() as session:
            stmt = (
                select(func.count)
                .select_from(DialogModel)
                .where(DialogModel.user_id == user_id)
            )
            dialogs_count = await session.execute(stmt)
        return dialogs_count.scalar_one_or_none()
