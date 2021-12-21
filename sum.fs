\ time gforth-fast sum.fs

: sum  ( n -- s )
    0
    swap 0 do
        i +
    loop ;

100000000 sum . cr
bye
