from django.shortcuts import render
from django.http import HttpResponseRedirect
 

def select(request):
    a = {"type" : []}
    with open("/home/vignesh/Documents/nandu/bell/media/config.txt",'r') as file:
        temp = file.read()
        for i in range(4):
            if(str(i) == temp ):
                a["type"].append({ "id" : i+1, "value" : "checked"})
                continue
            a["type"].append({"value" : "" , "id" : i+1})
        file.close()
        return render(request,"select.html",{ "select" : a })

def selectschedule(request):
    select = request.GET.get("schedule",0)
    with open("/home/vignesh/Documents/nandu/bell/media/config.txt",'w') as file:
        file.write(str(select))
    file.close()
    return HttpResponseRedirect("/showcurrent")
    
def show(request):
    temp = 0
    id = 0
    schedule = {"schedule" : []}
    with open("/home/vignesh/Documents/nandu/bell/media/config.txt",'r') as file:
        temp = file.read()
    with open("/home/vignesh/Documents/nandu/bell/media/schedule{}.txt".format(temp),'r') as file:
        while True:
            val = file.readline()
            id+=1
            schedule["schedule"].append({"id" : id , "time" : val})
            if(val == ""):
                break 
    return render(request,"show.html",{ "data" : schedule })

    


def add(request):
    time = request.GET.get('id',0)
    duration = request.GET.get('duration',0)
    with open("/home/vignesh/Documents/nandu/bell/media/config.txt",'r') as file:
        temp = file.read()
    with open("/home/vignesh/Documents/nandu/bell/media/schedule{}.txt".format(temp),'a+') as file:
        file.write("{} {}\n".format(time ,duration))
    file.close()
    return HttpResponseRedirect("/showcurrent")


def delete(request):
    delid = request.GET.get('id',0)
    temp = 0
    id = 0
    schedule = {"schedule" : []}
    with open("/home/vignesh/Documents/nandu/bell/media/config.txt",'r') as file:
        temp = file.read()
    with open("/home/vignesh/Documents/nandu/bell/media/schedule{}.txt".format(temp),'r') as file:
        while True:
            val = file.readline()
            id+=1
            schedule["schedule"].append({"id" : id , "time" : val})
            if(val == ""):
                break 
    with open("/home/vignesh/Documents/nandu/bell/media/schedule{}.txt".format(temp),'w+') as file:
        for i in schedule["schedule"]:
            if(i["id"] == int(delid) ):continue
            file.write("{}".format(i["time"]))
    file.close()
    return HttpResponseRedirect("/showcurrent")
    

def home(request):
    return render(request,"main.html")

def credit(request):
    return render(request,"credit.html")
