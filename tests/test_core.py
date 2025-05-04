import pandas as pd
from smart_todo_agent.core import prioritize_tasks

def test_prioritize_tasks_ordering():
    test_df = pd.DataFrame([
        {"name": "A", "deadline": "2025-05-10", "priority": 2, "duration": 1},
        {"name": "B", "deadline": "2025-05-08", "priority": 1, "duration": 1}
    ])
    test_df['deadline'] = pd.to_datetime(test_df['deadline'])
    prioritized = prioritize_tasks(test_df)
    assert prioritized.iloc[0]['name'] == 'B'
