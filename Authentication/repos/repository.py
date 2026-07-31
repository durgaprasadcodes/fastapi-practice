from .base import BaseRepo
from model import User
from schemas.user import UserInSignUp

class UserRepository(BaseRepo):
    def create_user(self,user:UserInSignUp):
        new_user = User(user.model_dump(exclude_none=True))
        self.db.add(instance=new_user)
        self.db.commit()
        self.db.refresh(instance=new_user)
        return {'user':new_user}
    def user_exist_by_email(self,email:str)->bool:
        user = self.db.query(User).filter_by(email=email).first()
        return user
    def get_user_by_id(self,user_id:int):
        user = self.db.query(User).filter(User.id == user_id).first()
        return user