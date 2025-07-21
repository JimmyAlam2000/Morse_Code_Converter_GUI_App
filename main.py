import tkinter as tk
from tkinter import messagebox

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/'
}

# Function to convert text to morse
def text_to_morse():
    text = entry.get()
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += '? '  # Unknown character
    output.delete('1.0', tk.END)
    output.insert(tk.END, morse_code)

# Function to clear input and output
def clear_all():
    entry.delete(0, tk.END)
    output.delete('1.0', tk.END)

# GUI setup
root = tk.Tk()
root.title("Text to Morse Code Converter")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Widgets
tk.Label(root, text="Enter Text:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Convert to Morse", command=text_to_morse, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=10)
tk.Button(root, text="Clear", command=clear_all, bg="#f44336", fg="white", font=("Arial", 11)).pack()

tk.Label(root, text="Morse Code Output:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
output = tk.Text(root, height=5, width=45, font=("Courier", 12))
output.pack(pady=5)

root.mainloop()
