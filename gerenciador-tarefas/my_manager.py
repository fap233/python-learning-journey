# this is a task list. for now just a placeholder
tasks = ["learn python", "do exercises", "config nvim" ]
print("--- My Tasks ---")
print(tasks) # for now just print the list how it is
print("----------------")

# this is just for me to see how can i add something (temporaly)
# lets learn
new_task = input("Type a new task to add: ")
tasks.append(new_task) #add the task to the list
print("List updated (just to see, not save): ")
print(tasks)
