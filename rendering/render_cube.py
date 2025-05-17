import trimesh
import numpy as np
vertices = np.array([
                [-1, -1, -1],
                [ 1, -1, -1],
                [ 1,  1, -1],
                [-1,  1, -1],
                [-1, -1,  1],
                [ 1, -1,  1],
                [ 1,  1,  1],
                [-1,  1,  1]
            ])
faces = np.array([
                [0, 1, 2], [0, 2, 3],
                [4, 7, 6], [4, 6, 5],
                [0, 4, 5], [0, 5, 1],
                [1, 5, 6], [1, 6, 2],
                [2, 6, 7], [2, 7, 3],
                [3, 7, 4], [3, 4, 0]
            ])
mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
edges = mesh.edges_unique
edge_lines = trimesh.load_path(mesh.vertices[edges])
edge_lines.colors = np.tile([0, 0, 0, 255], (len(edge_lines.entities), 1))

scene = trimesh.Scene()
scene.add_geometry(mesh)
scene.add_geometry(edge_lines)

scene.show()
