import requests
import json
import tkinter as tk


def get_github_info():
    repo_name = entry.get()
    url = f"https://api.github.com/users/{repo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info = {
            'company': data['company'],
            'created_at': data['created_at'],
            'email': data['email'],
            'id': data['id'],
            'name': data['login'],
            'url': data['url']
        }
        with open("github_info.json", "w") as file:
            json.dump(info, file)
            result_label.config(text="файлик готов hih)")
    else:
        result_label.config(text="мьмомьмомьмомьмомьмо(((( ашибка((((")


window = tk.Tk()
window.geometry("600x400")
window.title("poisk po imeni")
label = tk.Label(window, text="vvodi imya ^_^:")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="let's go", command=get_github_info)
button.pack()
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()