import asyncio
import os
import glob
import csv
from copilot import CopilotClient

def load_all_csvs_from_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(files)

    reading_list_by_year = {}

    for file in files:
        with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
            year = file.split('.')[0]
            reading_list_by_year[year] = ""
            for line in f:
                reading_list_by_year[year] += line + "\n"

    return reading_list_by_year

def build_prompt(csv_data, question):
    return f"""These are a csv files representing the books that I read by year: {csv_data}\n
    Based on the data, I would like to know: {question}
    """


async def main():
    client = CopilotClient()
    await client.start()

    session = await client.create_session({"model": "gpt-4.1"})
    # Example usage: load all CSVs from the 'CSVs' folder
    csv_folder = os.path.join(os.path.dirname(__file__), 'CSVs')

    csv_data = load_all_csvs_from_folder(csv_folder)
    
    prompt = build_prompt(csv_data, "How many books I read in 2025?")

    #print(f"Loaded CSV files: {list(csv_data.keys())}")

    response = await session.send_and_wait({"prompt": prompt})
    print(response.data.content)

    await client.stop()

asyncio.run(main())