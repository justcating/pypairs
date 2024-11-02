filename = "tasks.txt"
filename2 = "saved_tasks.txt"

def load_task(filename):
    tasks = []
    with open(filename, 'r', encoding='utf-8') as file:
        tasks = file.read().splitlines()
    return tasks

def save_task(filename2, tasks):
    with open(filename2, 'w', encoding='utf-8') as file:
        for task in tasks:
            file.write(task + '\n')
            
def add_task(tasks: list, task: str): # list, str, ... - types of arguments for comfortable work
    tasks.append(task)

def edit_task(tasks: list, indexOfEditingTask: int, newTask: str):
    tasks[indexOfEditingTask] = newTask

def delete_task(filename):
    tasks = load_task(filename)
    task_to_delete = input("Введіть завдання яке ви хочете видалити: ")
    updated_tasks = [task for task in tasks if task != task_to_delete]
    
    save_task(filename, updated_tasks)
def mark_ready_task(tasks: list, indexOfMarkingTask: int):
    tasks[indexOfMarkingTask] = f'"{tasks[indexOfMarkingTask]}" - DONE'

def main(tasks):
    print('tasks:', tasks)
    print('''\
    1. add new task
    2. edit existing task
    3. delete existing task
    4. mark existing task as done
    5. exit the program and save
    ''')

    userInput = input('choose option: ')

    if userInput == '1':
        add_task(tasks, input('name of new task: '))
        print('successfully added new task.')
    elif userInput == '2':
        edit_task(tasks, int(input('index of task to edit: ')), input('new name for task: '))
        print('successfully edited task.')
    elif userInput == '3':
        delete_task(filename, tasks)
        print('successfully deleted task.')
    elif userInput == '4':
        mark_ready_task(tasks, int(input('index of task to mark as done: ')))
        print('successfully marked task as done.')
    elif userInput == '5':
        save_task(filename2, tasks)
        print('Tasks saved successfully. Exiting...')
        return True
    else:
        print('Invalid option. Please choose again.')

tasks = load_task(filename)
while True:
    if main(tasks):
        break
main()