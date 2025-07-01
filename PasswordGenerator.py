import random
import string
import pyperclip as pc
import gradio as gr

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    try:
        length = int(length)
    except:
        return "Please enter a valid number."

    if length < 4:
        return "Password length should be at least 4."

    allChars = list(lower + upper + digits + symbols)
    password = random.sample(allChars, length)
    final_password = ''.join(password)

    pc.copy(final_password)
    return f"Your password is: {final_password} (Copied to clipboard)"

iface = gr.Interface(
    fn=generate_password,
    inputs=gr.Number(label="Password Length", value=12),
    outputs="text",
    title="Password Generator",
    description="Generates a secure random password and copies it to clipboard."
)

iface.launch()
