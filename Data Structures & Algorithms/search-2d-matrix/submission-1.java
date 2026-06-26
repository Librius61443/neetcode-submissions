class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix[0].length;
        int m = matrix.length;

        for(int i = 0; i < m; i++){
            if(matrix[i][n-1] >= target){
                for(int j : matrix[i]){
                    if(j == target) return true;
                }
                return false;
            }
        }

        return false;
    }
}
