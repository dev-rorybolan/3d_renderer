# 🧊 Tkinter 3D Shape Renderer

A Python-based GUI app built with Tkinter that lets you render various 3D geometric shapes in separate windows using `trimesh`. It was created as a creative final project for a school assignment—because who says school projects can't have rotating octahedrons?

---
## ✨ Features

- Simple Tkinter interface
- Dropdown menu to select 3D shapes
- Renders shapes in interactive viewer windows (via `trimesh.Scene`)
- Clean wireframe overlays for better visual clarity
- Uses separate scripts to avoid macOS GUI threading issues
---
## 🧱 Included Shapes

- Cube
- Tetrahedron
- Octahedron
- Icosahedron
- Capsule
- Torus
---
## 📦 Requirements

Make sure you have Python 3.10+ and the following libraries installed:

```bash
pip install trimesh numpy
```
Note for macOS users: trimesh.Scene.show() needs to run on the main thread. This app launches each render in its own subprocess to avoid crashes.

----
🚀 How to Run
Clone the repo:

```bash
git clone https://github.com/dev-rorybolan/3d_renderer.git
cd 3d_renderer
```
Run the main UI:

bash
Copy
Edit
python3 main.py
Choose a shape from the dropdown and click Load. A separate 3D viewer window will open with your selected shape.

---
Project Structure
- `main.py`
- `rendering/`
  - `render_cube.py`
  - `render_tetrahedron.py`
  - `render_octahedron.py`
  - `render_icosahedron.py`
  - `render_sphere.py`
  - `render_capsule.py`
  - `render_torus.py`



📌 Notes
This project is intentionally modular. Each shape is rendered by its own script for clarity and isolation.