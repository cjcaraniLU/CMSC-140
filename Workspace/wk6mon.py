from pathlib import Path

home_dir = r"/Users/cjcarani/Desktop/"
home_path = Path(home_dir)
print(home_path)

new_path = home_path / "pyth"
print(new_path)

path_to_proj = r"/Users/cjcarani/Desktop/pyth/"
base_path = Path(path_to_proj)
hwk_path = base_path / "Lab"
print(hwk_path)

print(Path.cwd())
