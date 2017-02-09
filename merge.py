import glob2
import datetime

all_content = ''
files = glob2.glob('merge/*.txt')

for file in files:
    with open(file, 'r') as f:
        all_content += f.read() + '\n'

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + '.txt', 'w') as f:
    f.write(all_content)
