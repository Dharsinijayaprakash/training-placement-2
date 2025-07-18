class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        int len = flowerbed.length;

        for (int i = 0; i < len; i++) {
            // Check if current plot is empty and adjacent plots are also empty or at boundary
            if (flowerbed[i] == 0 &&
                (i == 0 || flowerbed[i - 1] == 0) &&
                (i == len - 1 || flowerbed[i + 1] == 0)) {

                flowerbed[i] = 1; // Plant a flower here
                count++;

                if (count >= n) return true;
            }
        }

        return count >= n;
    }
}
