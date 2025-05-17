import trimesh
import numpy as np


phi = (1 + np.sqrt(5)) / 2
a, b = 1, phi

vertices = np.array([
                [-a,  b,  0],
                [ a,  b,  0],
                [-a, -b,  0],
                [ a, -b,  0],
                [ 0, -a,  b],
                [ 0,  a,  b],
                [ 0, -a, -b],
                [ 0,  a, -b],
                [ b,  0, -a],
                [ b,  0,  a],
                [-b,  0, -a],
                [-b,  0,  a]
            ])
faces = np.array([
                [0, 11, 5],
                [0, 5, 1],
                [0, 1, 7],
                [0, 7, 10],
                [0, 10, 11],
                [1, 5, 9],
                [5, 11, 4],
                [11, 10, 2],
                [10, 7, 6],
                [7, 1, 8],
                [3, 9, 4],
                [3, 4, 2],
                [3, 2, 6],
                [3, 6, 8],
                [3, 8, 9],
                [4, 9, 5],
                [2, 4, 11],
                [6, 2, 10],
                [8, 6, 7],
                [9, 8, 1]
        ])
mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

edges = mesh.edges_unique
edge_lines = trimesh.load_path(mesh.vertices[edges])
edge_lines.colors = np.tile([0, 0, 0, 255], (len(edge_lines.entities), 1))

scene = trimesh.Scene()
scene.add_geometry(mesh)
scene.add_geometry(edge_lines)

scene.show()
