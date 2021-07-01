import java.util.*;

class Solution {
    public static void main(String arg[]) {
        grayCode(3);
    }

    public static List<Integer> grayCode(int n) {
        List<Integer> list = new ArrayList<>();
        List<String> S_list = new ArrayList<>();


        for (int i = 0; i < Math.pow(2, n); i++) {
            String tmp = Integer.toBinaryString(i);
            for (int j = 0; j <= n; j++) {
                if (tmp.length() < n) {
                    tmp = "0" + tmp;
                }

            }
//            System.out.println(tmp);
            S_list.add(tmp);
        }

        for (int i = 0; i < S_list.size(); i++) {
            String tmp = S_list.get(i);
//            System.out.println(tmp);
            String gray = "";
            char s = tmp.charAt(0);
            gray += s;
            for (int j = 0; j < n-1; j++) {
                char a = tmp.charAt(j);
                char b = tmp.charAt(j + 1);
                int xor = (int) a ^ (int) b;
                gray += xor;
            }
//            System.out.println(gray);
            list.add(Integer.parseInt(gray, 2));
            System.out.println(list.get(i));
        }

        return list;
    }
}

//
//            000 000
//            001 001
//            010 011
//            011 010
//            100 110
//            101 111
//            110 101
//            111 100
