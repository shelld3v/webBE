from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_uuid: int):
    return db.query(models.User).filter(models.User.uuid == user_uuid).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = None
    uuid = None
    db_user = models.User(
        first_name = user.first_name,
        last_name = user.last_name,
        email=user.email, 
        hashed_password=hashed_password,
        uuid=uuid
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user