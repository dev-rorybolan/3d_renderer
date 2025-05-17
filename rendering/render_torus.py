import trimesh
import numpy as np


mesh = trimesh.creation.torus(1.0, 0.3)

edges = mesh.edges_unique
edge_lines = trimesh.load_path(mesh.vertices[edges])
edge_lines.colors = np.tile([0, 0, 0, 255], (len(edge_lines.entities), 1))

scene = trimesh.Scene()
scene.add_geometry(mesh)
scene.add_geometry(edge_lines)
scene.show()
