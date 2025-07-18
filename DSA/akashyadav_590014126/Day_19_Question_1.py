def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target: # to find the target element
            return mid

        if nums[left] <= nums[mid]: # to sort the left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1 
            else:
                left = mid + 1 

        else:   # to sort the right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

#example
print(search_rotated_array([4,5,6,7,0,1,2],6))