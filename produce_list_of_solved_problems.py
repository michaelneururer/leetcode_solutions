from os import listdir
f = open('README.md','w')
f.write(r'''
## My solutions to leet code problems.

| # | Title | Difficulty |
|---| ----- | ---------- |
''')
problems = []
for file in listdir():
    if file == 'produce_list_of_solved_problems.py' or file[-3:] != '.py':
        continue
    num, name, difficulty = file.rstrip('.py').split('_')
    problems.append([num,name,difficulty])
problems.sort(key=lambda x: x[0])
for prob in problems:
    f.write('|{0}|{1}|{2}|'.format(*prob))
    f.write('\n')
f.close()
