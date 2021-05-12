/*
因为密码学的特殊要求，快速幂取模必须底数和指数均上百位，使用python则需要自行写两个List进行更加复杂的高精度运算
因此使用Java语言调用BigInteger类
*/
import java.math.*;
import java.util.*;

public class SuperPow {

    public static void main(String [] args) {
        Scanner cin=new Scanner(System.in);


            BigInteger p=cin.nextBigInteger();
            BigInteger s=BigInteger.ZERO;
                BigInteger a=cin.nextBigInteger();
                BigInteger b=cin.nextBigInteger();
                BigInteger t=qpow(a,b,p);
                s=s.add(t).mod(p);

            System.out.println(s);

    }

    static BigInteger qpow(BigInteger a,BigInteger b,BigInteger p) {
        BigInteger s=BigInteger.ONE;//s=1
        BigInteger two=BigInteger.valueOf(2);
        while(!b.equals(BigInteger.ZERO)) {
            if((b.mod(two)).equals(BigInteger.ONE)) s=s.multiply(a).mod(p);
            a=a.multiply(a).mod(p);
            b=b.divide(two);
        }
        return s;
    }


}
