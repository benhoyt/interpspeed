# Run and benchmark all the interpreters
#
# Usage: python3 runall.py

import subprocess
import time

langs = [
    ('AWK (Mawk)', '1.3.4', 'mawk -f sum.awk', 'prints "5e+15"'),
    ('AWK (GoAWK)', '1.9.0', 'goawk -f sum.awk', ''),
    ('C (reference)', 'gcc 9.3.0', './sum', 'not interpreted; just a comparison'),
    ('Gforth', '0.7.9', 'gforth-fast --no-dynamic sum.fs', ''),
    ('Java (OpenJDK)', '14.0.2', 'java -Xint sum.java', 'JIT disabled'),
    ('Lua', '5.3.3', 'lua sum.lua', ''),
    ('LuaJIT (JIT off)', '2.1.0-beta3', 'luajit -joff sum.lua', 'JIT disabled; prints "4.99999995e+15"'),
    ('Perl', '5.30.0', 'perl sum.pl', ''),
    ('PHP', '7.4.3', 'php sum.php', ''),
    ('Python 2', '2.7.18', 'python2 sum.py', ''),
    ('Python 3', '3.10.0rc1', 'python3.10 sum.py', ''),
    ('Ruby', '2.7.0p0', 'ruby sum.rb', ''),
    ('Wren', '0.4.0', 'wren_cli sum.wren', 'prints "4.99999995e+15"'),
]

results = []
for lang, version, command, notes in langs:
    best = 1000000
    print('{} {} ({}) '.format(lang, version, command), end='', flush=True)
    for i in range(3):
        started = time.time()
        process = subprocess.run(command.split(), capture_output=True)
        elapsed = time.time() - started
        best = min(best, elapsed)
        print('.', end='', flush=True)
    print(' {} {}s'.format(process.stdout, best))
    results.append((lang, version, best, notes))

print()
print('Interpreter      | Version     | Time (s) | Notes')
print('---------------- | ----------- | -------- | -----')

results.sort(key=lambda r: r[2])
for lang, version, best, notes in results:
    print('{:16} | {:11} | {:8.2f} | {}'.format(lang, version, best, notes))
