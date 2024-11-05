
PaintGUI - Paint Application 🎨

PaintGUI is a basic paint program built with Python's Tkinter library for GUI design and the Python Imaging Library (PIL) for image saving and manipulation. Users can draw with customizable brush sizes and colors, clear the canvas, and save their artwork.

Features

🖌 Drawing: Click and drag on the canvas to draw with a customizable brush.
🔍 Brush Size: Adjust brush size with B+ and B- buttons.
🎨 Color Selection: Choose any brush color with a color picker.
🗑 Clear Canvas: Erase all drawings on the canvas.
💾 Save: Save your artwork as .png or .jpg.
❓ Exit Confirmation: Option to save changes before exiting.
Installation

Prerequisites
Python 3.x
Tkinter (included in Python's standard library)
Pillow (Python Imaging Library)
Install Pillow
Install Pillow via pip:

bash
Copy code
pip install pillow
Usage

Run the Application:
bash
Copy code
python paint_app.py
Controls:
Draw: Click and drag on the canvas to draw.
Clear: Clears the entire canvas.
Save: Saves the canvas content as an image.
Brush Size:
B+ button to increase brush size.
B- button to decrease brush size.
Color: Opens a color chooser to set the brush color.
Exit: Close the application window; you will be prompted to save your work if changes were made.
Code Structure

PaintGUI class: Contains the main functionality and GUI of the paint application.
Canvas: Tkinter's Canvas widget for drawing and user interaction.
PIL Image and ImageDraw: Used to maintain an internal image of the drawing, allowing for saving.
Brush Size Controls: Buttons to adjust brush width.
Color Picker: Opens a color chooser for selecting brush color.
Save and Exit Dialog: Asks to save before exiting, if necessary.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to download, modify, and enjoy your own drawing application with PaintGUI!
