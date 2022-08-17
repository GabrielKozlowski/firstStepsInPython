import requests
import json



def count_completed_tasks(tasks):
    tasksCompleted = dict()
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                tasksCompleted[entry["userId"]] += 1
            except KeyError:
                tasksCompleted[entry["userId"]] = 1
    return tasksCompleted

def get_user_with_top_completed_tasks(tasksCompleted):
    maxCompletedTasks = max(tasksCompleted.values())
    topScoreUserId = []
    for userId, score in tasksCompleted.items():
        if score == maxCompletedTasks:
            topScoreUserId.append(userId)
    return topScoreUserId

webSite = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = webSite.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    tasksCompleted = count_completed_tasks(tasks)
    topScoreUserId = get_user_with_top_completed_tasks(tasksCompleted)


#***Pobieranie danych JSON , wyszukaniu imienia id i wypisaniu***
#***Sposób pierwszy***
#
# webSite = requests.get("https://jsonplaceholder.typicode.com/users")
# users = webSite.json()
#
# for user in users:
#     if user["id"] in topScoreUserId:
#         print("Wręczamy ciasteczko mistrzunia dyscypliny do użytkownika o imieniu ",user["name"])

#***Sposób drugi wolny***

# for userId in topScoreUserId:
#     webSite = requests.get("https://jsonplaceholder.typicode.com/users",params="id="+str(userId))
#     user = webSite.json()
#     print("Wręczamy ciasteczko mistrzunia dyscypliny do użytkownika o imieniu ",user[0]["name"])
#

#***Sposób trzeci***
#
# def change_list_into_conj_of_param(my_list,key="id"):
#     conj_param = key + "="
#     lastIteration = len(my_list)
#     i = 0
#     for item in my_list:
#         i += 1
#         if (i == lastIteration):
#             conj_param += str(item)
#         else:
#             conj_param += str(item) + "&" + key + "="
#     return conj_param
#
#
# # conj_param  = change_list_into_conj_of_param(topScoreUserId)
# conj_param  = change_list_into_conj_of_param([5,7,10])
#
# webSite = requests.get("https://jsonplaceholder.typicode.com/users",params=conj_param)
#
# users = webSite.json()
# for user in users:
#     print("Wręczamy ciasteczko mistrzunia dyscypliny do użytkownika o imieniu ", user["name"] )
# ----------------------------------------------------------------------------------------------------




