// time java -Xint sum.java
public class Sum {
    public static void main(String[] args) {
        long s = 0;
        for (long i = 0; i < 100000000; i++) {
            s += i;
        }
        System.out.println(s);
    }
}
