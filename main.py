import tkinter
import tkinter.ttk as ttk
import subprocess
import sys

window = tkinter.Tk()
window.geometry('800x600')
window.title('3D Renderer')
window.resizable(True, True)

label = tkinter.Label(window, text='Select object to render')
label.pack(pady=10)
shapes = ["cube", "icosahedron", "octahedron", "tetrahedron", "torus", "capsule"]
dropdown = ttk.Combobox(window, values=shapes, state='readonly')
dropdown.pack(pady=10)

def load_shapes():
    match dropdown.get():
        case 'icosahedron':
            subprocess.Popen(["python3", "rendering/render_icosahedron.py"])
            sys.exit(0)
        case 'octahedron':
            subprocess.Popen(["python3", "rendering/render_octahedron.py"])
            sys.exit(0)
        case 'tetrahedron':
            subprocess.Popen(["python3", "rendering/render_tetrahedron.py"])
            sys.exit(0)
        case 'cube':
            subprocess.Popen(["python3", "rendering/render_cube.py"])
            sys.exit(0)
        case 'torus':
            subprocess.Popen(["python3", "rendering/render_torus.py"])
        case 'capsule':
            subprocess.Popen(["python3", "rendering/render_capsule.py"])
            sys.exit(0)

button = tkinter.Button(window, text='Load', command=load_shapes)
button.pack(pady=10)
window.mainloop()