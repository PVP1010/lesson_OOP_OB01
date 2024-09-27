class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = {
            'description': description,
            'deadline': deadline,
            'is_completed': False
        }
        self.tasks.append(task)
        print(f"Добавлена задача: {description}, Срок: {deadline}, Статус: Не выполнено")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['is_completed'] = True
            print(f"Задача '{self.tasks[index]['description']}' отмечена как выполненная.")
        else:
            print("Некорректный индекс задачи.")

    def get_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task['is_completed']]
        print("Текущие (не выполненные) задачи:")
        for task in pending_tasks:
            status = "Выполнено" if task['is_completed'] else "Не выполнено"
            print(f"Задача: {task['description']}, Срок: {task['deadline']}, Статус: {status}")


task_manager = Task()
task_manager.add_task("Купить продукты", "2024-09-15")
task_manager.add_task("Позвонить врачу", "2024-09-16")
task_manager.add_task("Закончить проект", "2024-09-20")

task_manager.mark_task_completed(0)
task_manager.mark_task_completed(4)

task_manager.get_pending_tasks()