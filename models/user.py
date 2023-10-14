#!/usr/bin/python3
"""
    This module defines the class User.
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User inherits from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
