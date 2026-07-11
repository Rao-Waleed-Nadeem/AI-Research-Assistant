from sqlalchemy import text
from app.models import Base

def test_database_connection(db_session):
    # Test if the in-memory sqlite database is up and we can execute a simple query
    result = db_session.execute(text("SELECT 1")).scalar()
    assert result == 1

def test_base_metadata():
    # Ensure Base is a valid declarative base
    assert hasattr(Base, "metadata")
