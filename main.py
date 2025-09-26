import customtkinter as ctk # Import customtkinter
from subprocess import run # Import run function from subprocess
from sys import exit as leave # Import leave function from sys

model_name = "abot" # Replace with the model that you choose
history = [] # History list

def add(msg, anchor): # Create add() function.
    lbl = ctk.CTkLabel(scroll_frame, text=msg, wraplength=380) # Wraplenght so it won’t leak outside
    lbl.pack(anchor=anchor) # Anchor it to the anchor given
    lbl.update() # Update the label
    return lbl # Return the label so we can configure it

def say(event=None): # Create the say() function
    global history # To use the variable that is not defined before
    try: # To catch an error
        text = entry.get() # Get the text from the entry
        if text: # If the text is not empty
            lt = text.lower() # To lowercase the text
            if lt=="/exit" or lt=="/quit" or lt=="/leave": # If user wants to leave
                root.destroy() # Destroy the window
                leave(0) # Quit the code
            if lt=="/clear" or lt=="/cls": # If user wants to clear the screen
                for widget in scroll_frame.winfo_children(): # Get all the widgets of the scroll frame
                    widget.destroy() # Destroy the widgets
                entry.delete(0, ctk.END) # Delete text inside the entry
                return # Return so it stops the function
            if lt=="/reset" or lt=="/restart": # If the user wants to reset
                for widget in scroll_frame.winfo_children(): # Get all the widgets of the scroll frame
                    widget.destroy() # Destroy the widgets
                history = [] # Make the list empty
                entry.delete(0, ctk.END) # Delete text inside the entry
                return # Return so it stops the function
            
            add(f"User: {text}", "e") # Add the prompt to the east
            loading_lbl = add("ABot: ...", "w") # Add the loading message to the west
            
            history_text = "\n".join(history) # Create the history text
            prompt = history_text + f"\nUser: {text}" # Create the final prompt

            try: # To catch an error
                result = run(["ollama", "run", model_name, prompt], text=True, capture_output=True, encoding="utf-8") # Give the prompt to the Ollama model
            except Exception as err: # If an error occured
                loading_lbl.configure(text=f"Error: {err}") # Replace the loading text with the error
            
            if result.stderr: # If error from ollama
                print(f"Error from Ollama: {result.stderr}") # Print the error
            
            loading_lbl.configure(text=f"ABot: {result.stdout.strip()}") # Replace the loading text with the result
            history.append(f"\nUser: {text}\nABot: {result.stdout.strip()}") # Add the history
            entry.delete(0, ctk.END) # Delete text inside the entry
    except Exception as err: # If an error occured
        print(f"An error occured: {err}") # Print the error

ctk.set_appearance_mode("dark") # Set appearance mode to dark

root = ctk.CTk() # Create the root
root.title("Chatbot") # Title the root as Chatbot

root.columnconfigure(0, weight=1) # Columnconfigure so the gui resizes according to the size of the window
root.rowconfigure(0, weight=1) # Rowconfigure so the gui resizes according to the size of the window

frame = ctk.CTkFrame(root) # Create the frame
frame.grid(row=0, column=0, sticky="nsew") # Put it in place

frame.columnconfigure(0, weight=1) # Columnconfigure so the gui resizes according to the size of the window
frame.rowconfigure(0, weight=1) # Rowconfigure so the gui resizes according to the size of the window

scroll_frame = ctk.CTkScrollableFrame(frame) # Create scroll frame
scroll_frame.grid(row=0, column=0, columnspan=2, sticky="nsew") # Put it in place 

entry = ctk.CTkEntry(frame) # Create entry
entry.grid(row=1, column=0, sticky="ew") # Put it in place
entry.bind("<Return>", say) # Bind it

entry_btn = ctk.CTkButton(frame, text="Say", command=say) # Create entry button
entry_btn.grid(row=1, column=1) # Put it in place

root.mainloop() # Run the main loop
