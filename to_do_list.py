class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print("Adding Task")
    
    def remove_task(self, index):
        if index >= 0 and index < len(self.tasks):
            del self.tasks[index]
            print("Removed Task")
        else:
            print("Invalid")
    
    def view_tasks(self):
        if self.tasks:
            print("Task: ")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("No Tasks")
    
def main():
        to_do_list = TodoList()
        
        while True:
            print("\nOptions:")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. View Task")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                task = input("Enter task ")
                to_do_list.add_task(task)
            elif choice == "2":
                index = int(input("Remove task ")) - 1
                to_do_list.remove_task(index)
            elif choice == "3":
                to_do_list.view_tasks()
            elif choice == "4":
                print("GoodBye")
                break
            else:
                print("Invalid choice")
                
if __name__ == "__main__":
    main()
    