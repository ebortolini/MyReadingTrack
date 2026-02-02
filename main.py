import asyncio
import os
from copilot import CopilotClient

def load_all_csvs_from_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    reading_list_by_year = {}

    for file in files:
        with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
            year = file.split('.')[0]
            reading_list_by_year[year] = ""
            for line in f:
                reading_list_by_year[year] += line + "\n"

    return reading_list_by_year

async def main():
    client = CopilotClient()
    await client.start()

    session = await client.create_session({"model": "gpt-4.1"})

    csv_folder = os.path.join(os.path.dirname(__file__), 'CSVs')
    csv_data = load_all_csvs_from_folder(csv_folder)

    system_prompt = f"These are csv files representing the books that I read by year: {csv_data}\nUse this data to answer future questions about my reading habits."
    await session.send_and_wait({"prompt": system_prompt})

    user_input = ""
    while (user_input.lower() != "exit"):
        user_input = input("Ask a question about your reading habits: ")
        if (user_input.lower() == "exit"):
            break
        # Now only send the user's question
        response = await session.send_and_wait({"prompt": user_input})
        print(response.data.content)

    await client.stop()

asyncio.run(main())