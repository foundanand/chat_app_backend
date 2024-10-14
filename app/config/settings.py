from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Basic App Settings
    app_name: str = "ChatApp"
    environment: str = "development"  # Could be 'development', 'staging', or 'production'
    debug: bool = True

    # Database Settings
    mongo_url: str  # MongoDB connection URL from the .env file
    database_name: str  # Database name from the .env file

    # Kafka Settings
    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_chat_topic: str = "chat-messages"

    # # Google Auth Settings
    # google_client_id: str = ""
    # google_client_secret: str = ""
    # google_redirect_uri: str = ""

    # # Apple Auth Settings
    # apple_client_id: str = ""
    # apple_team_id: str = ""
    # apple_key_id: str = ""
    # apple_private_key: str = ""  # Should be stored securely

    class Config:
        env_file = ".env"  # Load variables from a .env file if present

# Create an instance of Settings
settings = Settings()
