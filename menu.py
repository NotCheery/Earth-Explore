#Game menu file
import tkinter as tk
from tkinter import messagebox

def show_menu(start_game_callback):
    def start_game():
        menu_root.destroy()
        start_game_callback()
        
    def show_instructions():
        instructions = ("Welcome!")
        messagebox.showinfo("Instructions", instructions)
        
    def exit_game():
        confirm_exit = messagebox.askyesno("Are you sure you want to exit?")
        if confirm_exit:
            menu_root.destroy()
            exit()
    
    #Create menu
    menu_root = tk.Tk()
    menu_root.title("Earth Discovery")
    menu_root.geometry("400x300")
    
    # Menu Widgets
    tk.Label(menu_root, text="Earth Discovery", font=("Arial", 24, "bold")).pack(pady=20)
    tk.Button(menu_root, text="Start Game", font=("Arial", 16), command=start_game).pack(pady=10)
    tk.Button(menu_root, text="Instructions", font=("Arial", 16), command=show_instructions).pack(pady=10)
    tk.Button(menu_root, text="Exit", font=("Arial", 16), command=exit_game).pack(pady=10)
    
    #run menu
    menu_root.mainloop()
    
