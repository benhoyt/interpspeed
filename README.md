
# Interpreter speed comparison

```
python3 runall.py
```

Interpreter      | Version     | Time (s) | Notes
---------------- | ----------- | -------- | -----
C (reference)    | gcc 9.3.0   |     0.03 | not interpreted; just a comparison
Gforth           | 0.7.9       |     0.28 | 
LuaJIT (JIT off) | 2.1.0-beta3 |     0.42 | JIT disabled; prints "4.99999995e+15"
Lua              | 5.3.3       |     0.81 | 
PHP              | 7.4.3       |     0.91 | 
Java (OpenJDK)   | 14.0.2      |     2.53 | JIT disabled
AWK (Mawk)       | 1.3.4       |     2.75 | prints "5e+15"
Ruby             | 2.7.0p0     |     3.41 | 
Wren             | 0.4.0       |     3.76 | prints "4.99999995e+15"
Perl             | 5.30.0      |     5.11 | 
AWK (GoAWK)      | 1.9.0       |     6.31 | 
Python 2         | 2.7.18      |     7.72 | 
Python 3         | 3.10.0rc1   |     9.72 | 
