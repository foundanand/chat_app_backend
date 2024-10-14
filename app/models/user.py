from pydantic import BaseModel, Field, EmailStr, constr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    userFirstName: str = Field(..., description="User's first name")
    userLastName: Optional[str] = Field(None, description="User's last name")
    userName: str = Field(..., description="User's unique username for login")
    userEmail: EmailStr = Field(..., description="User's unique email for login")
    userPassword: str = Field(..., description="User's password, must have at least 8 characters")
    createdAt: datetime = Field(default_factory=datetime.timestamp, description="Date and time when the user was created")
    updatedAt: datetime = Field(default_factory=datetime.timestamp, description="Date and time when the user was last updated")
