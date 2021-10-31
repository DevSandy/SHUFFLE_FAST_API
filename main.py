import pymysql as pymysql
import uvicorn
from fastapi import FastAPI, status, Response
from Models.UserModel import CreateUser, UpdateUser, BanUser, DeactivateUser, LoginUser, CheckUserName

app = FastAPI(docs_url="/documentation", redoc_url=None)


@app.post("/")
@app.get("/")
async def index():
    return "Na Na Nigga on Fire"


# @app.put("/create_user")
# async def create_user(userdata: CreateUser, response: Response):
#     conn = pymysql.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         passwd="",
#         db="shuffle",
#         autocommit=True
#     )
#     try:
#         cur = conn.cursor()
#         cur.execute("INSERT INTO shuffle_users (user_uid,full_name,user_name,phone,gender,email,bio,profile_pic,latitude,longitude,device_token) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (userdata.user_uid, userdata.full_name, userdata.user_name, userdata.phone, userdata.gender, userdata.email, "I there, i'm on Shuffle ❤ ", userdata.profile_pic, userdata.latitude, userdata.longitude, userdata.device_token))
#         cur.close()
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM shuffle_users WHERE user_uid = %s AND isban = 0", userdata.user_uid)
#         user_account = cur.fetchone()
#         cur.close()
#         response.status_code = status.HTTP_200_OK
#         return {
#             "message": "User Created Successfully",
#             "user_information": {
#                 "user_uid": user_account[0],
#                 "full_name": user_account[1],
#                 "user_name": user_account[2],
#                 "phone": user_account[3],
#                 "email": user_account[4],
#                 "dob": user_account[5],
#                 "gender": user_account[6],
#                 "bio": user_account[7],
#                 "profile_pic": user_account[8],
#                 "facebook_url": user_account[9],
#                 "twitter_url": user_account[10],
#                 "instagram_url": user_account[11],
#                 "profession": user_account[12],
#                 "passion": user_account[13],
#                 "verified": user_account[16],
#                 "device_token": user_account[17],
#             }
#         }
#     except pymysql.Error as e:
#         response.status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
#         return {
#             "message": str(e)
#         }
#
#
# @app.post("/update_user")
# async def update_user(userdata: UpdateUser, response: Response):
#     conn = pymysql.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         passwd="",
#         db="shuffle",
#         autocommit=True
#     )
#     try:
#         cur = conn.cursor()
#         cur.execute("UPDATE shuffle_users SET full_name = %s, phone = %s, email = %s, dob = %s, gender = %s, bio = %s, facebook_url = %s, twitter_url = %s, instagram_url = %s, profession = %s, passion = %s, latitude = %s, longitude = %s, device_token = %s WHERE user_uid = %s", (userdata.full_name, userdata.phone, userdata.email, userdata.dob, userdata.gender, userdata.bio, userdata.facebook_url, userdata.twitter_url, userdata.instagram_url, userdata.profession, userdata.passion, userdata.latitude, userdata.longitude, userdata.device_token, userdata.user_uid))
#         cur.close()
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM shuffle_users WHERE user_uid = %s AND isban = 0", userdata.user_uid)
#         user_account = cur.fetchone()
#         cur.close()
#         response.status_code = status.HTTP_200_OK
#         return {
#             "message": "User Updated Successfully",
#             "user_information": {
#                 "user_uid": user_account[0],
#                 "full_name": user_account[1],
#                 "user_name": user_account[2],
#                 "phone": user_account[3],
#                 "email": user_account[4],
#                 "dob": user_account[5],
#                 "gender": user_account[6],
#                 "bio": user_account[7],
#                 "profile_pic": user_account[8],
#                 "facebook_url": user_account[9],
#                 "twitter_url": user_account[10],
#                 "instagram_url": user_account[11],
#                 "profession": user_account[12],
#                 "passion": user_account[13],
#                 "verified": user_account[16],
#                 "device_token": user_account[17],
#             }
#         }
#     except pymysql.Error as e:
#         response.status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
#         return {
#             "message": str(e)
#         }
#
#
# @app.post("/ban_user")
# async def ban_user(userdata: BanUser, response: Response):
#     conn = pymysql.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         passwd="",
#         db="shuffle",
#         autocommit=True
#     )
#     try:
#         cur = conn.cursor()
#         cur.execute("UPDATE shuffle_users SET isban = 1 WHERE user_uid = %s", userdata.user_uid)
#         cur.close()
#         response.status_code = status.HTTP_200_OK
#         return {
#             "message": "User Ban Successfully"
#         }
#     except pymysql.Error as e:
#         response.status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
#         return {
#             "message": str(e)
#         }
#
#
# @app.post("/deactivate_user")
# async def deactivate_user(userdata: DeactivateUser, response: Response):
#     conn = pymysql.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         passwd="",
#         db="shuffle",
#         autocommit=True
#     )
#     try:
#         cur = conn.cursor()
#         cur.execute("UPDATE shuffle_users SET isdeactivated = 1 WHERE user_uid = %s", userdata.user_uid)
#         cur.close()
#         response.status_code = status.HTTP_200_OK
#         return {
#             "message": "User Deactivated Successfully"
#         }
#     except pymysql.Error as e:
#         response.status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
#         return {
#             "message": str(e)
#         }
#
#
# @app.post("/login_user_or_get_user_details")
# async def login_user_or_get_user_details(userdata: LoginUser, response: Response):
#     conn = pymysql.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         passwd="",
#         db="shuffle",
#         autocommit=True
#     )
#     try:
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM shuffle_users WHERE user_uid = %s AND isban = 0", userdata.user_uid)
#         user_account = cur.fetchone()
#         cur.close()
#         if user_account:
#             response.status_code = status.HTTP_200_OK
#             if user_account[19] == 1:
#                 cur = conn.cursor()
#                 cur.execute("UPDATE shuffle_users SET isdeactivated = 0 WHERE user_uid = %s", userdata.user_uid)
#                 cur.close()
#             return {
#                 "message": "Login Successfull",
#                 "user_information": {
#                     "user_uid": user_account[0],
#                     "full_name": user_account[1],
#                     "user_name": user_account[2],
#                     "phone": user_account[3],
#                     "email": user_account[4],
#                     "dob": user_account[5],
#                     "gender": user_account[6],
#                     "bio": user_account[7],
#                     "profile_pic": user_account[8],
#                     "facebook_url": user_account[9],
#                     "twitter_url": user_account[10],
#                     "instagram_url": user_account[11],
#                     "profession": user_account[12],
#                     "passion": user_account[13],
#                     "verified": user_account[16],
#                     "device_token": user_account[17],
#                 }
#             }
#         else:
#             response.status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
#             return {
#                 "message": "User Not Found"
#             }
#     except pymysql.Error as e:
#         response.status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
#         return {
#             "message": str(e)
#         }
#
#
# @app.post("/check_user_name_is_available")
# async def check_user_name_is_available(userdata: CheckUserName, response: Response):
#     conn = pymysql.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         passwd="",
#         db="shuffle",
#         autocommit=True
#     )
#     try:
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM shuffle_users WHERE user_name = %s", userdata.user_name)
#         useraccounts = cur.fetchone()
#         cur.close()
#         if useraccounts:
#             response.status_code = status.HTTP_226_IM_USED
#             return {
#                 "message": "Username Already Exist"
#             }
#         else:
#             response.status_code = status.HTTP_200_OK
#             return {
#                 "message": "Username Available"
#             }
#     except pymysql.Error as e:
#         response.status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
#         return {
#             "message": str(e)
#         }
#

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
