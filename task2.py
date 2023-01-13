from pprint import pprint
import json
c=open('Movies_Detail.json',"r")
r=c.read()
movie_list=json.loads(r)
# pprint(movie_list)

def group_by_year():
    years_list=[]
    dict={}
    for i in movie_list:
        # print(i)
        year=i["year_of_release"]
        # print(year)
        movie_list2=[]
        if year not in years_list:
            years_list.append(year)
            for movie1 in movie_list:
                if movie1["year_of_release"]==year:
                    movie_list2.append(movie1)
                else:
                    pass
            dict[year]=movie_list2
        print(dict)
    return dict
movie_dict=group_by_year()
pprint(movie_dict)
with open("task2.json","w") as f:
    k=json.dump(movie_dict,f,indent=4)

