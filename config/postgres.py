import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

ENV = os.getenv("ENV", "development")

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/prod_db"


engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession)
