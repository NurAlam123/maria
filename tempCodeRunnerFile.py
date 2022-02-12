import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

con_maria = pymongo.MongoClient(os.getenv("DB"))
db = con_maria["fibu"]  # database
tb = db["other_data"]  # table
# tb.delete_one({"name": "chat_info"})
# tb.insert_one({"name": "chat_info"})
# # maria_acc_id = info.get("maria")
# tb.update_one({"name": "chat_info_test"}, {"$set": {
#     "2345": {
#         "maria": 2345,
#     }
# }})
info = tb.find_one({"name": "chat_info"})
print(info)

### data structure ###
# data = {
#     name: "chat_info_test",
#     1234: {
#         maria: 1234,
#         channel: 1234
#     },
#     2345: {
#         maria: 2345,
#         channel: 2345
#     }
# }
##########