import trimesh
import numpy as np

vertices = np.array([
                [1, 0, 0],
                [-1, 0, 0],
                [0, 1, 0],
                [0, -1, 0],
                [0, 0, 1],
                [0, 0, -1]
            ])
faces = np.array([
                [0, 4, 2],
                [2, 4, 1],
                [1, 4, 3],
                [3, 4, 0],
                [0, 2, 5],
                [2, 1, 5],
                [1, 3, 5],
                [3, 0, 5]
            ])
mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
edges = mesh.edges_unique
edge_lines = trimesh.load_path(mesh.vertices[edges])
edge_lines.colors = np.tile([0, 0, 0, 255], (len(edge_lines.entities), 1))

scene = trimesh.Scene()
scene.add_geometry(mesh)
scene.add_geometry(edge_lines)

scene.show()