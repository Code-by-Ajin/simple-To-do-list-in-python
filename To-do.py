import json
import os
import sys
from dataclasses import asdict, dataclass
from typing import List


@dataclass
class Task:
    id: int
    title: str
    is_completed: bool = False

    def mark_complete(self) -> None:
        self.is_completed = True


class TodoManager:
    def __init__(self, storage_file: str = "tasks.json") -> None:
        self.storage_file = storage_file
        self.tasks: List[Task] = []
        self._next_id: int = 1
        self._load_tasks()

    def add_task(self, title: str) -> Task:
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = Task(id=self._next_id, title=title.strip())
        self.tasks.append(task)
        self._next_id += 1
        self.save_tasks()
        return task

    def remove_task(self, task_id: int) -> bool:
        initial_length = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        if len(self.tasks) < initial_length:
            self.save_tasks()
            return True
        return False

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                self.save_tasks()
                return True
        return False

    def save_tasks(self) -> None:
        try:
            with open(self.storage_file, "w", encoding="utf-8") as f:
                serialized = [asdict(task) for task in self.tasks]
                json.dump(serialized, f, indent=4)
        except IOError as e:
            print(f"\n[Error] Failed to write data: {e}", flush=True)

    def _load_tasks(self) -> None:
        if not os.path.exists(self.storage_file):
            return
        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task(**item) for item in data]
                if self.tasks:
                    self._next_id = max(task.id for task in self.tasks) + 1
        except Exception:
            self.tasks = []


def display_menu() -> None:
    # Explicitly flushing the output forces the terminal to show it instantly
    print("\n" + "=" * 30, flush=True)
    print("      TASK MANAGER CLI", flush=True)
    print("=" * 30, flush=True)
    print("1. View Tasks", flush=True)
    print("2. Add Task", flush=True)
    print("3. Mark Task Complete", flush=True)
    print("4. Remove Task", flush=True)
    print("5. Exit", flush=True)
    print("=" * 30, flush=True)


def main() -> None:
    manager = TodoManager()
    
    # Simple direct startup print to make sure it's alive
    print("Initializing Task Manager App...", flush=True)

    while True:
        display_menu()
        
        # Safe input handling
        sys.stdout.write("Select an option (1-5): ")
        sys.stdout.flush()
        choice = sys.stdin.readline().strip()

        if choice == "1":
            print("\n--- Current Tasks ---", flush=True)
            if not manager.tasks:
                print("No tasks found.", flush=True)
            for task in manager.tasks:
                status = "✅" if task.is_completed else "❌"
                print(f"[{task.id}] {task.title} ({status})", flush=True)

        elif choice == "2":
            sys.stdout.write("\nEnter task title: ")
            sys.stdout.flush()
            title = sys.stdin.readline().strip()
            try:
                task = manager.add_task(title)
                print(f"Added: '{task.title}' (ID: {task.id})", flush=True)
            except ValueError as e:
                print(f"[Error] {e}", flush=True)

        elif choice == "3":
            sys.stdout.write("\nEnter Task ID to complete: ")
            sys.stdout.flush()
            try:
                task_id = int(sys.stdin.readline().strip())
                if manager.complete_task(task_id):
                    print(f"Task [{task_id}] complete.", flush=True)
                else:
                    print(f"ID {task_id} not found.", flush=True)
            except ValueError:
                print("Please enter a number.", flush=True)

        elif choice == "4":
            sys.stdout.write("\nEnter Task ID to remove: ")
            sys.stdout.flush()
            try:
                task_id = int(sys.stdin.readline().strip())
                if manager.remove_task(task_id):
                    print(f"Task [{task_id}] deleted.", flush=True)
                else:
                    print(f"ID {task_id} not found.", flush=True)
            except ValueError:
                print("Please enter a number.", flush=True)

        elif choice == "5":
            print("\nGoodbye!", flush=True)
            break
        else:
            print("Invalid choice.", flush=True)


if __name__ == "__main__":
    main()
