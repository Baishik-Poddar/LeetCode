class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        int i=0,j=0,flag=0;
        int n= nums.length;
        for(i=0;i<n-1;i++)
        {
            for(j=i+1;j<=n-1;j++)
            {
                if((nums[i]+nums[j]) == target)
                {
                    flag=1;
                    System.out.printf("a[%d]+a[%d]= %d%n", i,j,target);
                    System.out.printf("%d+%d = %d%n%n",nums[i],nums[j],target);
                    break;
                }
            }
            if(flag==1)
                    break;
        }
     return new int[]{i,j};
    }
}