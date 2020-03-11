class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
    int[] nums = new int[nums1.length+nums2.length];
	for(int i=0;i<nums1.length;i++){
		 nums[i] = nums1[i];
	 }
	
	for(int j=0;j<nums2.length;j++){
		 nums[nums1.length+j] = nums2[j];
	 }
	
	for(int i=0;i<nums.length;i++){
		for(int j=i;j<nums.length;j++){
			if(nums[i]>nums[j]){
				int tmp;
				tmp = nums[i];
				nums[i] = nums[j];
				nums[j] = tmp;
			}
		}
		
	}
	double ss;
	if(nums.length%2==0){
		ss = ((double)nums[(nums.length/2)-1]+(double)nums[nums.length/2])/2;
	}else{
		ss = (double)nums[nums.length/2];
        ss = (int)ss;
	}
        return ss;
    }
}