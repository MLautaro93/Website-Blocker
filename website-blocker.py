import tkinter as tk

# Window
root = tk.Tk()
root.geometry('384x256')
root.resizable(False, False)
root.config(bg = 'purple')
root.title('Website Blocker')

# Host path and IP adress
host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_adress = '127.0.0.1'

# Variable
url = tk.StringVar()

# Labels
header_label = tk.Label(text = 'Website Blocker', font = 'hermida 15 bold', fg = 'white', bg = 'black')
header_label.pack()
enter_label = tk.Label(text = 'Enter website:', font = 'hermida 10 bold', fg = 'white', bg = 'purple')
enter_label.place(relx = .5, y = 75, anchor = tk.CENTER)
info_label = tk.Label(font = 'hermida 10 bold', fg = 'white', bg = 'purple')
info_label.place(relx = .5, y = 200, anchor = tk.CENTER)

# Entry
url_entry = tk.Entry(width = 40, textvariable = url, justify = 'center')
url_entry.place(relx = .5, y = 100, anchor = tk.CENTER)

# Functions
def block():
    website = url.get()
    link = website.replace('www.', '')
    w_link = 'www.' + link    
    with open(host_path, 'r+') as file:
        content = file.read()
        if website not in content:
            file.write(ip_adress + ' ' + w_link + '\n')
            file.write(ip_adress + ' ' + link + '\n')
            info_label.config(text = 'Blocked', bg = 'red')
        else: 
            info_label.config(text = 'Already blocked', bg = 'red')
        file.close()

def unblock():
    website = url.get()
    with open(host_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        if any(website in line for line in content):
            for line in content:
                if website not in line:
                    file.write(line)
            file.truncate()
            info_label.config(text = 'Unblocked', bg = 'green')
        else:
            info_label.config(text = 'Already unblocked', bg = 'green')
        file.close()
    
                    
# Buttons
block_button = tk.Button(text = 'Block', fg = 'red', bg = 'black', command = block)
block_button.place(relx = .4, y = 150, anchor = tk.CENTER)
unblock_button = tk.Button(text = 'Unblock', fg = 'green', bg = 'black', command = unblock)
unblock_button.place(relx = .6, y = 150, anchor = tk.CENTER)

root.mainloop()