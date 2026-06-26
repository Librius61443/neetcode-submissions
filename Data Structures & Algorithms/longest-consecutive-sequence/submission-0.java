class Solution {
    public int longestConsecutive(int[] nums) {
        int n = nums.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        int res = 0;

        for(int i : nums){
            if(!map.containsKey(i)){
                map.put(i, map.getOrDefault(i-1, 0) + map.getOrDefault(i+1, 0) + 1);
                map.put(i - map.getOrDefault(i-1, 0), map.get(i));
                map.put(i + map.getOrDefault(i+1, 0), map.get(i));
                res = Math.max(res, map.get(i));
            }
        }

        return res;
    }
}
