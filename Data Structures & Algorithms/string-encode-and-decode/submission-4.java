class Solution {

    public String encode(List<String> strs) {
        String res = new String();

        for(String cur : strs){
            res += cur.length() + "#" + cur;
        }

        return res;
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int start = 0;
        while(start < str.length()){
            int end = start;
            while(str.charAt(end) != '#'){
                end++;
            }
            int length = Integer.valueOf(str.substring(start, end));
            start = end + 1;
            end = start + length;
            res.add(str.substring(start, end));
            start = end;
        }

        return res;
    }
}
