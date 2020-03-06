class Solution {
    public int[] twoSum(int[] nums, int target) {
    	int a = 0;
    	int b = 0;
        for(int i = 0;i < nums.length;i++){
            for(int j = i;j < nums.length;j++){
                if((nums[i]+nums[j])==target&&(i!=j)){
                	a = i;
                	b = j;
                    break;
                }
            }
        }
        int[] num = new int[2];
        num[0] = a;
        num[1] = b;
        return num;
    }
}