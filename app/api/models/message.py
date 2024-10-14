from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List
from user import User

class Message(BaseModel):
    messageTitle: Optional[str] = Field(None, description="Message title")
    messageContent: str = Field(..., description="Message content from the sender to the receiver")
    messageSender: User = Field(..., description="User who sent the message")
    messageUpdatedAt: datetime = Field(default_factory=datetime.timestamp, description="Date and time when the message was last updated")
    messageReadAt: Optional[datetime] = Field(None, description="Date and time when the message was read by the receiver")
    messageFiles: Optional[List[str]] = Field(None, description="List of aws s3 files attached to the message, originally uploaded by the sender on the server")
    messageReceiver: User = Field(..., description="User who will receive the message")
    messageCreatedAt: datetime = Field(default_factory=datetime.timestamp, description="Date and time when the message was created")
