tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def to_do_list():
    uncompleted_task = []  
    for task in tasks:
        if task["completed"] == False:
            uncompleted_task.append(task["description"])
    print(uncompleted_task)


def done_list():
    completed_task = []
    for task in tasks:
        if task["completed"] == True:
            completed_task.append(task["description"])
    print(completed_task)


def all_tasks():
    task_descriptions=[]
    for task in tasks:
        task_descriptions.append(task["description"])
    print(task_descriptions)

def task_duration(time):
    list_of_tasks=[]
    for task in tasks:
        if task["time_taken"] >= time:
            list_of_tasks.append(task["description"])
    print(list_of_tasks)

def task_description_is(text):
    for task in tasks:
        if task["description"] == text:      
            print(task)

def task_completed(text):
    for task in tasks:
        if task["description"] == text and task["completed"] == False:
            task["completed"] = True
        return tasks

tasks.append(
    {
        "description": "Do Homework",
        "completed": False,
        "time_taken": 120 
}
)


# to_do_list() 
# done_list()
# all_tasks()
# task_duration(20)
# task_description_is("Wash Dishes")



# print("Menu:")
# print("1: Display All Tasks")
# print("2: Display Uncompleted Tasks")
# print("3: Display Completed Tasks")
# print("4: Mark Task as Complete")
# print("5: Get Tasks Which Take Longer Than a Given Time")
# print("6: Find Task by Description")
# print("7: Add a new Task to list")
# print("M or m: Display this menu")
# print("Q or q: Quit")

# user_input = input("What do you want to do?" )