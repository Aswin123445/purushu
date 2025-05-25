from assets.keyword import search_prefixes
def extract_search_query(command: str) -> str:
    command = command.lower()
    for prefix in search_prefixes:
        if command.startswith(prefix):
            return command[len(prefix):].strip()
    return command 