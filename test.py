from src.classes.file import File
from src.classes.directory import Directory

# Crear directorio raíz

# Generar archivos de forma dinámica
files = [File(f'file{i}.txt', content=f'Contenido del archivo {i}') for i in range(1, 6)]
root_directory = Directory('root', r'C:\Users\ASADA\Desktop\py_projects\protor', [])


# Crear directorios y archivos anidados dinámicamente
def create_directories(depth: int, parent_directory: Directory):
    if depth == 0:
        return
    
    # Crear subdirectorios
    for i in range(1, 2):  # Crear 3 subdirectorios por cada nivel
        subdir_name = f'subdir{depth}_{i}'
        subdir = Directory(subdir_name, [])
        
        # Añadir subdirectorio al directorio padre
        parent_directory.add_entry(subdir)
        
        # Recursivamente agregar subdirectorios en el siguiente nivel
        create_directories(depth - 1, subdir)

# Llamar a la función para crear directorios hasta una profundidad de 3
create_directories(900, root_directory)

# Escribir el directorio raíz y su contenido, que incluye subdirectorios y archivos
root_directory.write_self()
