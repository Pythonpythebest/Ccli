# ======================
# Imports
# ======================
import socket
import platform
import os
import datetime
import requests
import psutil
import subprocess
import base64
import shutil


# ======================
# Colored print function
# ======================
def printc(text, color="white", end="\n"):
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m",
    }
    color_code = colors.get(color.lower(), colors["white"])
    print(f"{color_code}{text}{colors['reset']}", end=end)


# ======================
# Main app class
# ======================
class App:

    @staticmethod
    def ShowCommands():
        printc("================ Commands ================", "blue")
        printc("seeip           → Show local IP", "cyan")
        printc("info            → Show system info", "cyan")
        printc("createfile      → Create a file (usage: createfile <name> <text>)", "cyan")
        printc("rfile           → Delete a file (usage: rfile <name>)", "cyan")
        printc("rename          → Rename a file (usage: rename <old> <new>)", "cyan")
        printc("mkdir           → Create a directory (usage: mkdir <dirname>)", "cyan")
        printc("rdir            → Delete a directory (usage: rdir <dirname>)", "cyan")
        printc("copyfile        → Copy file (usage: copyfile <src> <dst>)", "cyan")
        printc("openfile        → Open file (usage: openfile <filename>)", "cyan")
        printc("tree            → Show directory structure", "cyan")
        printc("time            → Show current date and time", "cyan")
        printc("whoami          → Show current logged-in user", "cyan")
        printc("ls              → List files in current directory", "cyan")
        printc("calc            → Simple calculator (usage: calc <expression>)", "cyan")
        printc("specs           → Show system specs", "cyan")
        printc("cd              → Change directory", "cyan")
        printc("encode          → Encode message", "cyan")
        printc("decode          → Decode message", "cyan")
        printc("meme            → Get meme from API", "cyan")
        printc("swiki           → Search Wikipedia", "cyan")
        printc("clear           → Clear the screen", "cyan")
        printc("exit            → Exit the program", "cyan")
        printc("==========================================", "blue")

    @staticmethod
    def SeeIP():
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        printc(f"Device Name: {hostname}", "green")
        printc(f"Local IP: {local_ip}", "green")

    @staticmethod
    def Info():
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        plat = platform.platform()
        pythonversion = platform.python_version()
        printc(f"Device Name: {hostname}", "green")
        printc(f"Local IP: {local_ip}", "green")
        printc(f"Python Version: {pythonversion}", "cyan")
        printc(f"Platform: {plat}", "cyan")

    @staticmethod
    def CreateFile(filename, value):
        try:
            with open(filename, "w") as f:
                f.write(value)
            printc(f"✅ File '{filename}' created successfully!", "green")
        except Exception as e:
            printc(f"❌ Error creating file '{filename}': {e}", "red")

    @staticmethod
    def rfile(file):
        try:
            os.remove(file)
            printc(f"🗑️  Deleted file '{file}' successfully!", "yellow")
        except FileNotFoundError:
            printc(f"❌ File '{file}' not found!", "red")
        except Exception as e:
            printc(f"⚠️  Error deleting file '{file}': {e}", "red")

    @staticmethod
    def renFile(old_name, new_name):
        try:
            os.rename(old_name, new_name)
            printc(f"Renamed '{old_name}' to '{new_name}'", "green")
        except FileNotFoundError as a:
            printc(f"File not found: {a}", "red")
        except Exception as e:
            printc(f"Error: {e}", "red")

    @staticmethod
    def mkdir(dirname):
        try:
            os.makedirs(dirname)
            printc(f"📁 Directory '{dirname}' created!", "green")
        except FileExistsError:
            printc(f"⚠️  Directory '{dirname}' already exists!", "yellow")
        except Exception as e:
            printc(f"❌ Error creating directory '{dirname}': {e}", "red")

    @staticmethod
    def rdir(dirname):
        try:
            os.rmdir(dirname)
            printc(f"🗑️  Directory '{dirname}' deleted!", "yellow")
        except FileNotFoundError:
            printc(f"❌ Directory '{dirname}' not found!", "red")
        except OSError:
            printc(f"⚠️  Directory '{dirname}' is not empty!", "red")
        except Exception as e:
            printc(f"❌ Error deleting directory '{dirname}': {e}", "red")

    @staticmethod
    def Time():
        now = datetime.datetime.now()
        printc(f"📅 Date: {now.strftime('%Y-%m-%d')}", "green")
        printc(f"⏰ Time: {now.strftime('%H:%M:%S')}", "green")

    @staticmethod
    def whoami():
        try:
            user = os.getlogin()
            printc(f"👤 Current User: {user}", "green")
        except Exception as e:
            printc(f"❌ Error: {e}", "red")

    @staticmethod
    def ls():
        try:
            files = os.listdir()
            printc("📂 Current Directory Files:", "cyan")
            for f in files:
                if os.path.isdir(f):
                    printc(f" [DIR] {f}", "blue")
                else:
                    printc(f" - {f}", "green")
        except Exception as e:
            printc(f"❌ Error listing files: {e}", "red")

    @staticmethod
    def calc(eq):
        try:
            result = eval(eq)
            printc(f"🧮 Result: {result}", "green")
        except Exception as e:
            printc(f"❌ Invalid expression: {e}", "red")

    @staticmethod
    def Memes():
        url = "https://api.apileague.com/retrieve-random-meme?keywords=rocket"
        api_key = "953d886fc2a74fd08a1106596c4c9096"
        headers = {'x-api-key': api_key}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            meme = data[0] if isinstance(data, list) else data
            title = meme.get("title", "No title found")
            description = meme.get("description", "No description provided")
            image_url = meme.get("image", "No image URL found")

            printc("🎭 Random Meme Retrieved!", "magenta")
            printc(f"Title: {title}", "cyan")
            printc(f"Description: {description}", "green")
            printc(f"Image URL: {image_url}", "yellow")

        except Exception as e:
            printc(f"❌ Error retrieving meme: {e}", "red")

    @staticmethod
    def swiki(query):
        try:
            import wikipedia
            summary = wikipedia.summary(query)
            printc(summary, "green")
        except Exception:
            printc("❌ An error happened retrieving Wikipedia summary", "red")

    @staticmethod
    def Show_Specs():
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            cores = psutil.cpu_count(logical=True)
            freq = psutil.cpu_freq()
            mem = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            stats = psutil.cpu_stats()

            printc("🧠 System Information", "blue")
            printc(f"CPU Usage: {cpu_usage}% ({cores} cores)", "green")
            printc(f"CPU Frequency: {freq.current:.2f} MHz", "cyan")
            printc(f"Context Switches: {stats.ctx_switches}", "yellow")
            printc(f"Interrupts: {stats.interrupts}", "yellow")
            printc(f"Soft Interrupts: {stats.soft_interrupts}", "yellow")
            printc(f"System Calls: {stats.syscalls}", "yellow")
            printc(f"RAM Usage: {mem.percent}% ({mem.used // (1024**2)} MB / {mem.total // (1024**2)} MB)", "magenta")
            printc(f"Disk Usage: {disk.percent}% ({disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB)", "magenta")

        except Exception as e:
            printc(f"❌ Error retrieving system info: {e}", "red")

    @staticmethod
    def Encode(message):
        try:
            encoded_message = base64.b64encode(message.encode('utf-8')).decode('utf-8')
            printc(f"💬 Encoded message: {encoded_message}", "magenta")
        except Exception as e:
            printc(f"❌ Error encoding message: {e}", "red")

    @staticmethod
    def Decode(encoded_input):
        try:
            decoded_message = base64.b64decode(encoded_input.encode('utf-8')).decode('utf-8')
            printc(f"💬 Decoded message: {decoded_message}", "green")
        except Exception as e:
            printc(f"❌ Error decoding message: {e}", "red")

    @staticmethod
    def RunFile(Command):
        try:
            subprocess.run([Command], shell=True)
        except Exception as e:
            printc(e, "red")

    @staticmethod
    def cd_command(path):
        try:
            os.chdir(path)
            printc(f"Changed directory to: {os.getcwd()}", "green")
        except FileNotFoundError:
            printc(f"Directory not found: {path}", "red")
        except NotADirectoryError:
            printc(f"Not a directory: {path}", "red")
        except PermissionError:
            printc(f"Permission denied: {path}", "red")

    @staticmethod
    def tree(path="."):
        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level
            printc(f"{indent}📁 {os.path.basename(root)}/", "cyan")
            sub_indent = " " * 4 * (level + 1)
            for f in files:
                printc(f"{sub_indent}- {f}", "green")


# ======================
# Main loop
# ======================
if __name__ == "__main__":
    a = App()
    printc("Welcome to the Python CLI App!", "magenta")
    printc("Type 'help' to see all commands.\n", "cyan")

    while True:
        cmd = input(f"{os.getcwd()}>> ").strip().split()

        if not cmd:
            continue

        command = cmd[0].lower()

        match command:
            case "help":
                a.ShowCommands()

            case "seeip":
                a.SeeIP()

            case "info":
                a.Info()

            case "createfile":
                if len(cmd) < 3:
                    printc("Usage: createfile <filename> <text>", "yellow")
                else:
                    filename = cmd[1]
                    text = " ".join(cmd[2:])
                    a.CreateFile(filename, text)

            case "rfile":
                if len(cmd) < 2:
                    printc("Usage: rfile <filename>", "yellow")
                else:
                    a.rfile(cmd[1])

            case "rename":
                if len(cmd) < 3:
                    printc("Usage: rename <old_name> <new_name>", "yellow")
                else:
                    a.renFile(cmd[1], cmd[2])

            case "mkdir":
                if len(cmd) < 2:
                    printc("Usage: mkdir <dirname>", "yellow")
                else:
                    a.mkdir(cmd[1])

            case "rdir":
                if len(cmd) < 2:
                    printc("Usage: rdir <dirname>", "yellow")
                else:
                    a.rdir(cmd[1])

            case "time":
                a.Time()

            case "whoami":
                a.whoami()

            case "ls":
                a.ls()

            case "calc":
                if len(cmd) < 2:
                    printc("Usage: calc <expression>", "yellow")
                else:
                    a.calc(" ".join(cmd[1:]))

            case "meme":
                a.Memes()

            case "specs":
                a.Show_Specs()

            case "swiki":
                if len(cmd) < 2:
                    printc("Usage: swiki <query>", "yellow")
                else:
                    a.swiki(" ".join(cmd[1:]))

            case "encode":
                if len(cmd) < 2:
                    printc("Usage: encode <message>", "yellow")
                else:
                    a.Encode(" ".join(cmd[1:]))

            case "decode":
                if len(cmd) < 2:
                    printc("Usage: decode <message>", "yellow")
                else:
                    a.Decode(" ".join(cmd[1:]))

            case "run":
                if len(cmd) < 2:
                    printc("Usage: run <command>", "yellow")
                else:
                    a.RunFile(" ".join(cmd[1:]))

            case "cd":
                if len(cmd) < 2:
                    printc("Usage: cd <directory>", "yellow")
                else:
                    a.cd_command(" ".join(cmd[1:]))

            case "tree":
                a.tree()

            case "copyfile":
                if len(cmd) < 3:
                    printc("Usage: copyfile <source> <destination>", "yellow")
                else:
                    try:
                        shutil.copy(cmd[1], cmd[2])
                        printc(f"📄 Copied '{cmd[1]}' → '{cmd[2]}'", "green")
                    except Exception as e:
                        printc(f"❌ Error copying file: {e}", "red")

            case "openfile":
                if len(cmd) < 2:
                    printc("Usage: openfile <filename>", "yellow")
                else:
                    file = " ".join(cmd[1:])
                    try:
                        if os.name == "nt":
                            os.startfile(file)
                        else:
                            subprocess.run(["xdg-open", file])
                        printc(f"📂 Opened '{file}'", "green")
                    except Exception as e:
                        printc(f"❌ Error opening file: {e}", "red")

            case "clear":
                os.system("cls" if os.name == "nt" else "clear")

            case "exit":
                printc("👋 Goodbye!", "magenta")
                break

            case _:
                printc("❌ Unknown command. Type 'help' for a list of commands.", "red")
