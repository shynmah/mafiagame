import random
print("----****welcome to mafia game****----")
finalroles=[]
users=[]
mafias=[]
for i in range(9):
    user=input("enter your name please : ")
    users.append(user)
print(users)
roles=["doctor","karagah","sniper","shahrvand","shahrvand","zereh push","Boss","lover","sharlatan"]
for item in roles:
    finalroles=random.sample(roles,k=9)
finalname=[[users[0],finalroles[0]],[users[1],finalroles[1]],[users[2],finalroles[2]],[users[3],finalroles[3]],[users[4],finalroles[4]],[users[5],finalroles[5]],[users[6],finalroles[6]],[users[7],finalroles[7]],[users[8],finalroles[8]]]
print(finalname)
# print("----****Day 1****----")
# user1=input(f"{users[0]} lotfan 30s sohbat konid : ")
# print(f"{users[0]} : {user1}")
# print("------------------------------------------------------------------------")
# user2=input(f"{users[1]} lotfan 30s sohbat konid : ")
# print(f"{users[1]} : {user2}")
# print("------------------------------------------------------------------------")
# user3=input(f"{users[2]} lotfan 30s sohbat konid : ")
# print(f"{users[2]} : {user3}")
# print("------------------------------------------------------------------------")
# user4=input(f"{users[3]} lotfan 30s sohbat konid : ")
# print(f"{users[3]} : {user4}")
# print("------------------------------------------------------------------------")
# user5=input(f"{users[4]} lotfan 30s sohbat konid : ")
# print(f"{users[4]} : {user5}")
# print("------------------------------------------------------------------------")
# user6=input(f"{users[5]} lotfan 30s sohbat konid : ")
# print(f"{users[5]} : {user6}")
# print("------------------------------------------------------------------------")
# user7=input(f"{users[6]} lotfan 30s sohbat konid : ")
# print(f"{users[6]} : {user7}")
# print("------------------------------------------------------------------------")
# user8=input(f"{users[7]} lotfan 30s sohbat konid : ")
# print(f"{users[7]} : {user8}")
# print("------------------------------------------------------------------------")
# user9=input(f"{users[8]} lotfan 30s sohbat konid : ")
# print(f"{users[8]} : {user9}")
# print("------------------------------------------------------------------------")
# print("----****night 1****----")
# print("mafia ha bidar shavand !!!")
# # print(finalname["lover"])
# # print(finalname["sharlatan"])
# # print(finalname["boss"])
# print("------------------------------------------------------------------------")
# mafia1=input("boss lotfan 30s sohbat konad : ")
# print(f"boss : {mafia1}")
# # print("------------------------------------------------------------------------")
# mafia2=input("lover lotfan 30s sohbat konid : ")
# print(f"lover : {mafia2}")
# # print("------------------------------------------------------------------------")
# mafia3=input("sharlatan lotfan 30s sohbat konid : ")
# print(f"sharlatan : {mafia3}")
# # print("------------------------------------------------------------------------")
shot1=input("shot emshab shoma kist ? ")
print(shot1)
save1=input("doctor che kasi ra save mikonid ? ")
print(save1)
for L in finalname:
    if save1==shot1:
        break
    try:
        L.remove(shot1)
    except ValueError:
        pass
kar1=input("estelame che kasi ra migirid ? ")
print(kar1)
# print("----****day 2****----")
# user1=input(f"{users[0]} lotfan 30s sohbat konid : ")
# print(f"{users[0]} : {user1}")
# print("------------------------------------------------------------------------")
# user2=input(f"{users[1]} lotfan 30s sohbat konid : ")
# print(f"{users[1]} : {user2}")
# print("------------------------------------------------------------------------")
# user3=input(f"{users[2]} lotfan 30s sohbat konid : ")
# print(f"{users[2]} : {user3}")
# print("------------------------------------------------------------------------")
# user4=input(f"{users[3]} lotfan 30s sohbat konid : ")
# print(f"{users[3]} : {user4}")
# print("------------------------------------------------------------------------")
# user5=input(f"{users[4]} lotfan 30s sohbat konid : ")
# print(f"{users[4]} : {user5}")
# print("------------------------------------------------------------------------")
# user6=input(f"{users[5]} lotfan 30s sohbat konid : ")
# print(f"{users[5]} : {user6}")
# print("------------------------------------------------------------------------")
# user7=input(f"{users[6]} lotfan 30s sohbat konid : ")
# print(f"{users[6]} : {user7}")
# print("------------------------------------------------------------------------")
# user8=input(f"{users[7]} lotfan 30s sohbat konid : ")
# print(f"{users[7]} : {user8}")
# print("------------------------------------------------------------------------")
# user9=input(f"{users[8]} lotfan 30s sohbat konid : ")
# print(f"{users[8]} : {user9}")
# print("------------------------------------------------------------------------")
# print("######  vote  ######")
# vote = []
# for i in range(9):
#     user=input("enter your name please : ")
#     vote.append(user)
# votedict={}
# i=0
# while i<=9:
#     votenum=vote.count(users[0])
#     votedict{users[0]:votenum}
#     i+=1
