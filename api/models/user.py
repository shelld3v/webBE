from typing import Any, Iterable, Optional
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
    

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)