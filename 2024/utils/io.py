def read_input(path: str) -> str: 
    with open(path, 'r') as f:
        data = f.read()
    return data
