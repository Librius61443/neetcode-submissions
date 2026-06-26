class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        Stack<int[]> st = new Stack<>();
        int [] res = new int[n];
        
        for(int i = 0; i < n; i++){
            int temp = temperatures[i];
            while(!st.isEmpty() && temp > st.peek()[0]){
                int[] cur = st.pop();
                res[cur[1]] = i - cur[1];
            }
            st.push(new int[]{temp, i});
        }

        return res;
    }
}
