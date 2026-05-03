class Solution 
{
    public boolean isPalindrome(int x) 
    {
      int r = 0, s=0, n=0;
      n=x;
      if(n<0)
      {
         n= n*(-1);
      }
      while(n!=0){  
      s=s*10+(n%10);
      n=n/10;}
      if(s == x)
      {
        return true;
      }
      else
      {
        return false;
      }
    }
}