class Solution:
    def firstSearch(self, arr, k):
        low = 0
        high = len(arr) - 1
        res = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == k:
                res = mid  # Record candidate index
                high = mid - 1  # Keep searching left for earlier occurrence
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1

        return res