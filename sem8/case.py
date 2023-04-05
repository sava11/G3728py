import shelve as sl
from time import sleep
from os import system
fname=''
class SAVE:
	def __init__(self):
		self.file=sl.open("sem8/"+fname)
	def save(self,v,n):
		self.file[n]=v
	def load(self,n):
		return self.file[n]
	def __del__(self):
		self.file.close()
s=None
data={}
def load():
    system("cls")
    data.update(s.load('!!!!!'))
    print("loaded")
    sleep(2)
def save():
    system("cls")
    s.save(data,'!!!!!')
    print("saved")
    sleep(2)
      
doings=[
	"Открыть файл",
    "Сохранить файл",
    "Посмотреть все контакты",
    "редактировать контакты",
    "Выход"
    ]
contacts_edits=[
    "Создать контакт",
    "Изменить контакт",
    "Найти контакт",
    "Удалить контакт",
    "выход"
]
def merge_dicts(x:dict, y:dict):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z
def print_contact(name:str,d:dict):
    print("Name: "+name)
    print("Number and comment:")
    for e in d.keys():
        print(e,d[e])
    print("-------------------------")
def print_data():
    system("cls")
    print("-------------------------")
    for e in data.keys():
        print_contact(e,data[e])
    input("press any key to exit")
    system("cls")
def print_only_data_keys():
    system("cls")
    print("-------------------------")
    for e in enumerate(data.keys()):
        print(e[0]+1,e[1])
        print("-------------------------")
    print(len(data.keys())+1,"exit")
    print("-------------------------")
def clamp(a,mx,mn):
    if a<mn:return mn
    elif a>mx:return mx
    else:return a

def search_string(string:str,what:str):
    word=""
    e=0
    i=0
    while e<len(string):
        if string[e]==what[i]:
            word+=what[i]
            i+=1
        if word==what:break
        e+=1
    return word==what

while True:
    system("cls")
    print("opened file is "+fname)
    for e in enumerate(doings):print(e[0]+1,e[1])
    print()
    var= input("what you choice?: ")
    match var:
        case "5":break
        case "3":
            print_data()
        case "1":
            data={}
            fname=input("input file name: ")
            s=SAVE()
            if len(list(s.file.keys()))!=0:load()
        case "2":
            if s!=None:
                save()
            else:
                print("error")
                sleep(2)
        case "4":
            while True:
                system("cls")
                for e in enumerate(contacts_edits):
                    print(e[0]+1,e[1])
                print()
                var= input("what you choice?: ")
                match var:
                    case "5":break
                    case "4":
                        while True:
                            system("cls")
                            for e in enumerate(data.keys()):
                                print(e[0]+1,e[1])
                            print(len(data.keys())+1,"exit")
                            i=input("who you wont to delete?: ")
                            if i==str(len(data.keys())+1):
                                break
                            for e in enumerate(list(data.keys())):
                                if str(e[0]+1)==i:
                                    data.pop(e[1])
                                    #print_data()
                    case "3":
                        while True:
                            system("cls")
                            print("input number to find prson from numbers")
                            print("input string to find prson from name")
                            print("for exit press enter")
                            print()
                            i=input("input: ")
                            system("cls")
                            if i!="":
                                if i.isdigit() and int(i)>=0:
                                    print("-------------------------")
                                    for e in data.keys():
                                        for num in data[e].keys():
                                            if i==num:
                                                print_contact(e,data[e])
                                    print()
                                    input("press any key to exit")
                                else:
                                    system("cls")
                                    print("-------------------------")
                                    have_any=False
                                    for e in data.keys():
                                        if search_string(e,i):
                                            print_contact(e,data[e])
                                            have_any=True
                                    if have_any==False:
                                        print("nothing")
                                    print()
                                    input("press any key to exit")
                            else:
                                break
                    case "2":
                        while True:  
                            print_only_data_keys()
                            print()
                            value=input("input value of person to edit: ")
                            if value==str(len(data.keys())+1):
                                break
                            cont_name=""
                            if value.isdigit() and int(value)>0:
                                while True:
                                    for e in enumerate(data.keys()):
                                        if e[0]+1==int(value):
                                            cont_name=e[1]
                                    system("cls")
                                    print("what you wont to edit:")
                                    print(1,"name")
                                    print(2,"numbers")
                                    print(3,"comments")
                                    print(4,"exit")
                                    choice=input("input value of parametr to edit: ")
                                    match choice:
                                        case "4":break
                                        case "3":
                                            while True:
                                                numbers=data[cont_name]
                                                system("cls")
                                                for e in enumerate(numbers):
                                                    print(e[0]+1,e[1],numbers[e[1]])
                                                print(len(numbers)+1,"exit")
                                                print()
                                                v1=input("what you choice to edit?: ")
                                                if v1==str(len(numbers)+1):
                                                    break
                                                for e in enumerate(numbers):
                                                    if e[0]+1==int(v1):
                                                        numbers[e[1]]=input("input comment: ")
                                                        break
                                        case "2":
                                            while True:
                                                numbers=data[cont_name]
                                                system("cls")
                                                for e in enumerate(numbers):
                                                    print(e[0]+1,e[1])
                                                print(len(numbers)+1,"add new phone number")
                                                print(len(numbers)+2,"exit")
                                                print()
                                                v1=input("what you choice to edit?: ")
                                                if v1==str(len(numbers)+2):
                                                    break
                                                if v1.isdigit() and int(v1)<len(numbers)+2:
                                                    num_comment=""
                                                    for e in enumerate(numbers):
                                                        if e[0]+1==int(v1):
                                                            num_comment=numbers[e[1]]
                                                            break
                                                    
                                                    i=input("input phone number: ")
                                                    unique=True
                                                    for e in data[cont_name].keys():
                                                        if e==i:unique=False
                                                    if unique==True:
                                                        if i=="":break
                                                        if num_comment=="":
                                                            num_comment=input("add comment?: ")
                                                        if i.isdigit() and int(i)>=0:
                                                            if int(v1)<len(numbers)+1:
                                                                data[cont_name]={i:num_comment}
                                                            else:
                                                                unique=True
                                                                for e in data[cont_name].keys():
                                                                    if e==i:unique=False
                                                                if unique==True:
                                                                    data[cont_name]=merge_dicts(data[cont_name],{i:num_comment})
                                                        else:
                                                            print("error")
                                                            sleep(2)
                                                    else:
                                                        print("error")
                                                        sleep(2)
                                                else:
                                                    print("error")
                                                    sleep(2)
                                        case "1":
                                            ch_cont_name=input("input person name: ")
                                            cont_data=data[cont_name]
                                            data.pop(cont_name)
                                            data[ch_cont_name]=cont_data
                            else:
                                print("error")
                                sleep(2)         
                    case "1":
                        system("cls")
                        print("to exit press enter")
                        cont_name=input("input person name: ")
                        if data.get(cont_name,"")!="":
                            print("this name already exists")
                            sleep(2)
                        else:
                            #person_comment=input("input person comment: ")  
                            numbers={}
                            while True:
                                i=input("input phone number: ")
                                if i=="":break
                                if i.isdigit() and int(i)>=0:
                                    numbers[i]=input("input number comment: ")
                                else:
                                    print("error")
                                    sleep(2)
                        data[cont_name]=numbers
