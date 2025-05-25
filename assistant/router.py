from modules import jokes, media, open_ai, weadher
from assets.keyword import weather_list,search_prefixes,todo_list
from assets.extract_search import extract_search_query 
def handle_command(command: str) -> str:

    if "joke" in command:
        return jokes.get_joke()

    elif "play" in command:
        return media.play_youtube_video(command)

    elif any(keyword in command for keyword in search_prefixes):
        search_word = extract_search_query(command)
        print(search_word)
        return media.search_google(search_word)

    elif "chat" in command or "codaa" in command:
        return open_ai.call_deepseek_api(command)
    elif "add task" in command or "remember" in command:
        task = command.replace("add task", "").replace("remember", "").strip()
        todo_list.append(task)
        return f"Task added: {task}"
    elif "list tasks" in command or "what's on my list" in command:
        if todo_list:
            tasks = "\n".join(f"{i+1}. {task}" for i, task in enumerate(todo_list))
            return f"Your tasks are:\n{tasks}"
        else :
            return "Your task list is empty."
    elif "remove task" in command:
        try:
            number = int(command.split()[-1]) - 1
            if 0 <= number < len(todo_list):
                removed = todo_list.pop(number)
                return f"Removed task: {removed}"
            else:
                return "That task number does not exist."
        except ValueError:
            return "Please say the number of the task to remove."

    elif "clear my list" in command or "clear tasks" in command:
        todo_list.clear()
        return "All tasks cleared."
    
    elif any(keyword in command for keyword in weather_list):
            return weadher.get_weather(command)

    elif "stop" in command or "exit" in command:
        return "Goodbye! Aswin"

    else:
        return "Sorry, I didn't understand that."