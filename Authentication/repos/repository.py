from .base import BaseRepo
from model import User
from schemas.user import UserInSignUp

class UserRepository(BaseRepo):
    def create_user(self,user:UserInSignUp):
        new_user = User(user.model_dump(exclude_none=True))
        self.session.add(instance=new_user)
        self.session.commit()
        self.session.refresh(instance=new_user)
        
        return {'user':new_user}
    def user_exit_by_email(self,email:str)->bool:
        user = self.session.query(User).filter_by(email=email).first()
        return user
    def get_user_by_id(self,user_id:int):
        user = self.session.query(User).filter(id == user_id).first()
        return user