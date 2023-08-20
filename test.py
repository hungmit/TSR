import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import messagebox, filedialog


def createwidgets():
    feedlable =lable(root, bg="steelblue", fg="white", text="Webcam part")

root = tk.Tk()
root.title("Pycam")
root.geometry("1340x700")
root.configure(background=skyblue)

createwidgets()
