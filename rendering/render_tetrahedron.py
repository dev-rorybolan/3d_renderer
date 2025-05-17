import trimesh
import numpy as np

vertices = np.array([
                [1, 1, 1],
                [-1, -1, 1],
                [-1, 1, -1],
                [1, -1, -1]
            ])
faces = np.array([
                [0, 1, 2],
                [0, 3, 1],
                [0, 2, 3],
                [1, 3, 2]
            ])
mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

edges = mesh.edges_unique
edge_lines = trimesh.load_path(mesh.vertices[edges])
edge_lines.colors = np.tile([0, 0, 0, 255], (len(edge_lines.entities), 1))

scene = trimesh.Scene()
scene.add_geometry(mesh)
scene.add_geometry(edge_lines)

scene.show()
