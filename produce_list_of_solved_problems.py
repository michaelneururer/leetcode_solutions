from os import listdir
f = open('README.md','w')
problems = []
for file in listdir():
    if file == 'produce_list_of_solved_problems.py' or file[-3:] != '.py' or file[-10:] == 'NOTDONE.py':
        continue
    num, name, difficulty = file.rstrip('py').rstrip('.').split('_')[1], '-'.join(file.rstrip('py').rstrip('.').split('_')[2:-1]), file.rstrip('py').rstrip('.').split('_')[-1]
    problems.append([num,name,difficulty])
problems.sort(key=lambda x: int(x[0]))
f.write(r'''
## My solutions to leet code problems.

Solved {0} easy problems, {1} medium problems, and {2} hard problems.

| # | Title | Difficulty |
|---| ----- | ---------- |
'''.format(len([prob for prob in problems if prob[2]=='easy']), len([prob for prob in problems if prob[2]=='medium']), len([prob for prob in problems if prob[2]=='hard'])))
for prob in problems:
    f.write('|{0}|{1}|{2}|'.format(*prob))
    f.write('\n')
f.close()
