from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os
load_dotenv()

MY_ENV_VAR = os.getenv('MONGO_URI')
client = MongoClient(MY_ENV_VAR, tlsAllowInvalidCertificates=True)

db = client["ytmanager"]
video_collection = db["videos"]

def add_video(name, time):
    video_collection.insert_one({"name":name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )      

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n youtube manager app ")
        print("1. list all videos")
        print("2. add new video")
        print("3. update a video")
        print("4. delete a video")
        print("5. exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)   
        elif choice == '3':
            video_id = input("Enter video id to be updated: ")
            name = input("Enter updated video name: ")
            time = input("Enter updated video time: ")
            update_video(video_id, name, time)   
        elif choice == '4':
            video_id = input("Enter video id to be deleted: ")            
            delete_video(video_id)   
        elif choice == '5':
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()