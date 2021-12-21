# time mawk -f sum.awk
BEGIN {
    for (i = 0; i < 100000000; i++) {
        s += i
    }
    print(s)
}
