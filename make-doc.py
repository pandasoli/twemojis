import os
files = os.listdir('.')

res =  "<div align='center'>\n"
res += '\n'
res += '| Emoji         | Emoji Unicode     |\n'
res += '| :-----------: | ----------------- |\n'

for file in files:
  name = file.split('.')[0]

  res += f"| <img src='{file}' rel='{name} emoji' width='22'/> | {name} |\n"

f = open('README.md', 'w')
f.write(res)
f.close()
