import java.util.Scanner;
class Solution {
    public int romanToInt(String s) 
    {
      Scanner sc = new Scanner(System.in);
      int sum=0;
      boolean fg=false;
      Map <Character, Integer> romandict = new HashMap<>();
      romandict.put('I',1);
      romandict.put('V',5);
      romandict.put('X',10);
      romandict.put('L',50);
      romandict.put('C',100);
      romandict.put('D',500);
      romandict.put('M',1000);
      for(int i=0; i<s.length();i++)
      {
        char schar = s.charAt(i);
        int val = romandict.get(schar);
        if(i<s.length()-1)
        {
            if(val < romandict.get(s.charAt(i+1)))
            {
                val= romandict.get(s.charAt(i+1))-val ;
                // i++;
                sum+=val;
                fg=true;
            }
            else
            {
                if(fg==false)
                    sum+=val;
                else
                {
                    fg=false;
                    continue;
                }

            }
        }
        else
        {
            if(fg==false)
                 sum+=val;
        }
    }
      return sum;
    }
}