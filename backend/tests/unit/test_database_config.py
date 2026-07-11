from app.db.database import DatabaseSettings

def test_database_settings_default():
    settings = DatabaseSettings()
    # Verify the default configuration string is a postgres URL
    assert "postgresql" in settings.DATABASE_URL
