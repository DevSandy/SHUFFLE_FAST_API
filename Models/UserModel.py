from pydantic import BaseModel


class CreateUser(BaseModel):
    user_uid: str
    full_name: str
    user_name: str
    phone: str
    email: str
    gender: str
    profile_pic: str
    latitude: str
    longitude: str
    device_token: str


class UpdateUser(BaseModel):
    user_uid: str
    full_name: str
    user_name: str
    phone: str
    email: str
    dob: str
    gender: str
    bio: str
    facebook_url: str
    twitter_url: str
    instagram_url: str
    profession: str
    passion: str
    profile_pic: str
    latitude: str
    longitude: str
    device_token: str


class BanUser(BaseModel):
    user_uid: str


class DeactivateUser(BaseModel):
    user_uid: str


class LoginUser(BaseModel):
    user_uid: str


class CheckUserName(BaseModel):
    user_name: str
