from search import retrieve_results
from tkinter import *
import webbrowser


start = 0
end = 10
results = list()

window = Tk()
window.title("Search Engine")
window.geometry('800x400')


def make_clickable(*args):
    index = results_box.curselection()[0]
    item = results_box.get(index)
    webbrowser.open_new(item)


def next_callback():
    prev_btn['state']= 'normal'
    global start
    global end
    results_box.delete(0, END)
    start = end
    end = end + 10 if end + 10 < len(results) else len(results)
    for r in results[start:end]:
        results_box.insert(END, r)
    if end >= len(results): next_btn['state'] = 'disable'


def previous_callback():
    global start
    global end
    next_btn['state']= 'normal'
    results_box.delete(0, END)
    start, end = start-10, end-10
    for r in results[start:end]:
        results_box.insert(END, r)

    if start <= 0: prev_btn['state'] = 'disable'


def clear_callback():
    global start
    global end
    global results
    start, end = 0, 10
    results = list()
    next_btn['state'], prev_btn['state'], clear_btn['state'] = 'disable', 'disable', 'disable'
    results_box.delete(0, END)
    search_box.delete(0, END)


def search_callback():
    global start
    global end
    global results
    start, end = 0, 10
    results_box.bind('<<ListboxSelect>>', make_clickable)
    next_btn['state'], prev_btn['state'], clear_btn['state'] = 'normal', 'disable', 'normal'
    results_box.delete(0, END)
    results = [r[0] for r in retrieve_results(search_box.get(), 'uic.edu')]
    for r in results[start:end]:
        results_box.insert(END, r)


search_box = Entry(window, justify=LEFT, width=50)
search_box.grid(column=0, row=0)

results_box = Listbox(window, justify=LEFT, width=80)
results_box.grid(column=0, row=1)

prev_btn = Button(window, justify=LEFT, anchor="w", text="Previous", command=previous_callback)
prev_btn.grid(column=0, row=2)
prev_btn['state'] = 'disable'

next_btn = Button(window, justify=LEFT, anchor="w", text="Next", command=next_callback)
next_btn.grid(column=1, row=2)
next_btn['state'] = 'disable'

search_btn = Button(window, justify=LEFT, text="Search", command=search_callback)
search_btn.grid(column=1, row=0)

clear_btn = Button(window, justify=LEFT, text="Clear", command=clear_callback)
clear_btn.grid(column=2, row=0)
clear_btn['state'] = 'disable'

window.mainloop()

