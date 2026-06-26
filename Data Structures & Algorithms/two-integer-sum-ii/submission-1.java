class Solution {
    public int[] twoSum(int[] nums, int target) {
        int end = nums.length -1;
        int start = 0;

        while(start < end){
            int sum = nums[start] + nums[end];
            if(sum > target)end--;
            else if(sum < target) start ++;
            else return new int[]{start + 1, end + 1};
        }

        return new int[]{0,0};
    }
}
