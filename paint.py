from tkinter import *
from PIL import ImageDraw, Image
from tkinter import filedialog, messagebox, colorchooser

WIDTH, HEIGHT = 500, 500
CENTER = WIDTH // 2
WHITE = (255, 255, 255)

class PaintGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("paint")
        self.brush_width = 15
        self.current_colour = "#000000"
        self.cnv = Canvas(self.root, width=WIDTH-19, height=HEIGHT-10, bg='white')
        self.cnv.pack()
        self.cnv.bind("<B1-Motion>", self.paint)

        self.image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        self.draw = ImageDraw.Draw(self.image)

        self.btn_frame = Frame(self.root)
        self.btn_frame.pack(fill=X)

        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)

        self.clear_btn = Button(self.btn_frame, text="clear", command=self.clear)
        self.clear_btn.grid(row=1, column=1, sticky=W+E)

        self.save_btn = Button(self.btn_frame, text="save", command=self.save)
        self.save_btn.grid(row=0, column=1, sticky=W+E)

        self.bplus_btn = Button(self.btn_frame, text="B+", command=self.bplus)
        self.bplus_btn.grid(row=1, column=2, sticky=W+E)

        self.bminus_btn = Button(self.btn_frame, text="B-", command=self.bminus)
        self.bminus_btn.grid(row=2, column=1, sticky=W+E)

        self.colour_btn = Button(self.btn_frame, text="colour", command=self.colour)
        self.colour_btn.grid(row=2, column=2, sticky=W+E)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def clear(self):
        self.cnv.delete("all")
        self.draw.rectangle([0, 0, 1000, 1000], fill="white")

    def paint(self, event):
        x1, y1 = (event.x-1), (event.y-1)
        x2, y2 = (event.x+1), (event.y+1)
        self.cnv.create_rectangle(x1, y1, x2, y2, fill=self.current_colour, outline=self.current_colour, width=self.brush_width)
        self.draw.rectangle([x1, y1, x2+self.brush_width, y2+self.brush_width], fill=self.current_colour, outline=self.current_colour)

    def bplus(self):
        self.brush_width += 1

    def bminus(self):
        if self.brush_width > 1:
            self.brush_width -= 1

    def save(self):
        filename = filedialog.asksaveasfilename(initialfile="untitled.png", defaultextension="png",
                                                filetypes=[("PNG", ".png"), ("JPG", ".jpg")])
        if filename != "":
            self.image.save(filename)

    def colour(self):
        _, self.current_colour = colorchooser.askcolor(title="Choose")

    def on_closing(self):
        answer = messagebox.askyesnocancel("Quit", "Do you want to save?", parent=self.root)
        if answer is not None:
            if answer:
                self.save()
            self.root.destroy()
            exit(0)

PaintGUI()
