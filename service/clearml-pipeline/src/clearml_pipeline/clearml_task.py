import logging

from clearml import Task
from utils_1.my_module_1 import function_1
from utils_2.my_module_2 import function_2

project_name = "Tutorial/dependencies_example"
task_name = "mono-repo dependency with poetry"
queue_name = "controller"

task = Task.init(project_name=project_name, task_name=task_name)
task.execute_remotely(queue_name=queue_name, clone=False, exit_process=True)


print("Hello from clearml_task.py")
function_1()
function_2()
print("Bye from clearml_task.py")
