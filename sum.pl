# time perl sum.pl
my @s = 0;
for (my $i = 0; $i < 100000000; $i++) {
    $s += $i;
}
print "$s\n";
