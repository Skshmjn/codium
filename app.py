from datetime import datetime
import os
from subprocess import call

import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)


def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')


def print_todo():
    clear()
    print("***********************TODO List**********************")
    task_list = redis_client.lrange('todo', 0, -1)
    if not len(task_list) is 0:
        for task in task_list:
            print(task.decode("utf-8"))
    else:
        print()
        print("############# No tasks for you ###################")
    print()


def add_entry():
    clear()
    print("............................................................")
    print()
    new_task_name = input("Enter a new for your new task: ")
    if new_task_name != "":
        redis_client.rpush('todo', str(datetime.now().strftime("%d-%b-%Y (%H:%M)") + " -----> " + new_task_name))


def delete_entry():
    clear()
    task_list = redis_client.lrange('todo', 0, -1)
    if not len(task_list) is 0:
        for task in task_list:
            print(task_list.index(task) + 1, ")", task.decode("utf-8"))

    print()

    if len(task_list) != 0:
        try:
            task_to_remove = int(input("Choose a task to remove: "))

            if task_to_remove <= len(task_list):
                print("*******************task done***************************")
                print()
                redis_client.lrem('todo', 0, redis_client.lindex('todo', task_to_remove - 1))
        except ValueError:
            print("Task can't be deleted")
            input()


def main_loop():
    while 1:
        print_todo()

        print("1) Add a new task")
        print("2) Task has been done ")
        print("3) Exit")
        print()

        action = int(input("Choose an option: "))

        try:

            if action is 1:
                add_entry()
            elif action is 2:
                delete_entry()
            elif action is 3:
                break

        except ValueError:
            print("invalid argument")
            input()


if __name__ == '__main__':
    main_loop()
