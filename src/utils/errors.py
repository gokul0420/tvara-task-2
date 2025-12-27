def safe_run(func):
    try:
        return func()
    except Exception as e:
        print(f"Error : {e}")
        return None