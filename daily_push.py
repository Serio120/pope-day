import datetime

def update_file():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"Registro automatico: {current_time}\n")

if __name__ == "__main__":
    update_file()