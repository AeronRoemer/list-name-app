import pymongo
import environ
env = environ.Env()
environ.Env.read_env()

MONGO_PASSWORD = env('MONGO_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://user1:{MONGO_PASSWORD}@cluster0.jd2cj.mongodb.net/react-api-test?retryWrites=true&w=majority")
db = client.test