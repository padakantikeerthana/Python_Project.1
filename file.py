from pathlib import Path

path = Path('example.txt')
print(path.name)

from pathlib import Path

path = Path()
for file in path.glob('*.py'):
  print(file)

from pathlib import Path

path = Path()
for file in path.glob('*'):
  print(file)
