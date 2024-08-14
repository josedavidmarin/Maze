import matplotlib.pyplot as plt
import numpy as np
import random

def generate_maze(width, height):
    maze = np.zeros((height, width), dtype=np.int8)
    
    # Función recursiva para la generación del laberinto
    def carve_passages_from(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < width and 0 <= ny < height and maze[ny, nx] == 0:
                maze[ny, nx] = 1
                maze[y + dy//2, x + dx//2] = 1
                carve_passages_from(nx, ny)
    
    # Iniciar la generación desde la esquina superior izquierda
    carve_passages_from(0, 0)
    
    return maze

def draw_maze(maze):
    plt.figure(figsize=(10, 10))
    plt.imshow(maze, cmap=plt.cm.binary, interpolation='none')
    plt.xticks([])  # Oculta los ejes x
    plt.yticks([])  # Oculta los ejes y
    plt.show()

# Tamaño del laberinto
width, height = 21, 21  # Debe ser impar para tener paredes entre celdas

# Generar y dibujar el laberinto
maze = generate_maze(width, height)
draw_maze(maze)
