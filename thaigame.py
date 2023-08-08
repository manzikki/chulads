import tkinter as tk
import random

# Define the Thai verbs and their English translations
flashcards = {
    "กิน": "to eat",
    "นอน": "to sleep",
    "วิ่ง": "to run",
    "ดู": "to see/watch",
    "พูด": "to speak/talk",
    "เรียน": "to study",
    "ไป": "to go",
    "มา": "to come",
    "เปิด": "to open",
    "ปิด": "to close",
    "เขียน": "to write",
    "อ่าน": "to read",
    "เป็น": "to be",
    "มี": "to have",
    "รู้": "to know",
    "เห็น": "to see",
    "อยู่": "to stay",
    "ใช้": "to use",
    "เชื่อ": "to believe",
    "รัก": "to love",
    "คิด": "to think",
    "เลือก": "to choose",
    "เปลี่ยน": "to change",
    "เจอ": "to meet",
    "เข้า": "to enter",
    "ออก": "to exit",
    "ขาย": "to sell",
    "ซื้อ": "to buy",
    "เขียน": "to write",
    "อยาก": "to want",
    "ชอบ": "to like",
    "ช่วย": "to help",
    "ดื่ม": "to drink",
    "ฟัง": "to listen",
    "รอ": "to wait",
    "แนะนำ": "to introduce",
    "ให้": "to give",
    "เรียก": "to call",
    "ร้อง": "to sing",
    "ร้อน": "to be hot",
    "หิว": "to be hungry",
    "เห็นด้วย": "to agree",
    "ไม่เห็นด้วย": "to disagree",
    "ทำ": "to do",
    "รู้จัก": "to know (someone)",
    "นั่ง": "to sit",
    "ยิ้ม": "to smile",
    "หัด": "to learn",
    "ขับ": "to drive",
    "นั่ง": "to sit",
    "ยืน": "to stand",
    "ว่ายน้ำ": "to swim",
    "กรีด": "to cry",
}

def show_flashcard():
    # Randomly select a flashcard
    thai_word = random.choice(list(flashcards.keys()))
    english_translation = flashcards[thai_word]
    
    # Update the labels
    thai_label.config(text=thai_word)
    english_label.config(text=english_translation)

# Create the main window
window = tk.Tk()
window.title("Thai Verbs Flashcards")

# Create the labels for the flashcards
thai_label = tk.Label(window, text="", font=("Arial", 24))
thai_label.pack(pady=20)

english_label = tk.Label(window, text="", font=("Arial", 18))
english_label.pack(pady=10)

# Create the "Next" button
next_button = tk.Button(window, text="Next", command=show_flashcard)
next_button.pack(pady=10)

# Show the first flashcard
show_flashcard()

# Start the main event loop
window.mainloop()
