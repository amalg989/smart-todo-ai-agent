from datetime import datetime, timedelta
import pandas as pd

def load_tasks(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df['deadline'] = pd.to_datetime(df['deadline'], errors='coerce')
    return df.dropna(subset=['deadline'])

def prioritize_tasks(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by=['deadline', 'priority'])

def schedule_tasks(df: pd.DataFrame, start_time: datetime) -> list:
    schedule = []
    now = start_time
    for _, task in df.iterrows():
        end = now + timedelta(hours=task['duration'])
        schedule.append({
            "task": task['name'],
            "start": now.strftime('%H:%M'),
            "end": end.strftime('%H:%M')
        })
        now = end
    return schedule
