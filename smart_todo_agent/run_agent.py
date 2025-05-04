from smart_todo_agent.core import load_tasks, prioritize_tasks, schedule_tasks
from datetime import datetime

def main():
    df = load_tasks('data/tasks.csv')
    prioritized = prioritize_tasks(df)
    now = datetime.now().replace(minute=0, second=0, microsecond=0)
    result = schedule_tasks(prioritized, now)

    print("=== Your Smart Schedule ===")
    for task in result:
        print(f"{task['task']} – {task['start']} to {task['end']}")

if __name__ == "__main__":
    main()
