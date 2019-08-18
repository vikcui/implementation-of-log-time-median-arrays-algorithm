# author : YANG CUI
# idea taken from the URL: https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
# the following code was implemented by myself. I'm not really good at coding so please bear with me.
# This file contains a program that finds the median from two sorted arrays merging together in logarithmic time.

nums1 = [1,2]
nums2 = [3,4,5]



# input validation not needed for this but should be implemented in the future.
def checkMedian(nums1, nums2, x=None, x_dash=None,y=None,y_dash=None,median=False):
    """
    This function given two sorted arrays as inputs returns the value if the median is found, otherwise, return false.
    :param median:
    :param nums1, nums2 sorted arrays
    :return the value of median if median is found, false otherwise.
    """
    # odd array
    if (len(nums1) + len(nums2)) % 2 == 1:
        if x != None and x_dash != None and y != None and y_dash != None:
            if nums1[x] >= nums2[y] and nums1[x] <= nums2[y_dash]:
                median = nums1[x]
                return median
            elif nums1[x] <= nums2[y] and nums1[x_dash] >= nums2[y]:
                median = nums2[y]
                return median
            else:
                return False
        elif x == None and x_dash != None and y != None and y_dash == None:
            if nums1[x_dash] >= nums2[y]:
                median = nums2[y]
                return median
            else:
                return False
        elif x != None and x_dash == None and y != None and y_dash != None:
            if nums2[y] >= nums1[x]:
                median = nums2[y]
                return median
            elif nums1[x] >= nums2[y] and nums1[x] <= nums2[y_dash]:

                median = nums1[x]
                return median
            else:
                return False
    # even array
    else:
        if x != None and x_dash != None and y != None and y_dash != None:
            if nums1[x] >= nums2[y] and nums1[x] <= nums2[y_dash]:
                if nums1[x_dash] <= nums2[y_dash]:
                    median = (nums1[x] + nums1[x_dash])/2
                elif nums1[x_dash] > nums2[y_dash]:
                    median = (nums1[x] + nums2[y_dash])/2
                return median
            elif nums1[x] <= nums2[y] and nums1[x_dash] >= nums2[y]:
                if nums2[y_dash] <= nums1[x_dash]:
                    median = (nums2[y] + nums2[y_dash])/2
                elif nums2[y_dash] > nums1[x_dash]:
                    median = (nums2[y] + nums1[x_dash])/2
                return median
            else:
                return False
        elif x == None and x_dash != None and y != None and y_dash == None:
            if nums1[x_dash] >= nums2[y]:
                median = (nums2[y] + nums1[x_dash])/2
                return median
            else:
                return False
        elif x != None and x_dash == None and y != None and y_dash != None:
            if nums2[y] >= nums1[x]:
                median = (nums2[y] + nums2[y_dash])/2
                return median
            elif nums1[x] >= nums2[y] and nums1[x] <= nums2[y_dash]:
                median = (nums1[x] + nums2[y_dash])/2
                return median
            else:
                return False
        elif x != None and x_dash == None and y == None and y_dash != None:
            if nums1[x] <= nums2[y_dash]:
                median = (nums1[x] + nums2[y_dash])/2
                return median
            else:
                return False
        elif x == None and x_dash != None and y != None and y_dash != None:
            if nums2[y] <= nums1[x_dash]:
                if nums1[x_dash]<= nums2[y_dash]:
                    median = (nums2[y] + nums1[x_dash])/2
                    return median
                elif nums1[x_dash] > nums2[y_dash]:
                    median = (nums2[y] + nums2[y_dash])/2
                    return median
            else:
                return False


def sorted_median(nums1,nums2):
    # the case where one of the arrays is null
    if len(nums1) == 0 or len(nums2) == 0:
        if len(nums1) == 0 and len(nums2) != 0:
            if len(nums2) % 2 == 1:
                median = nums2[len(nums2)//2]
                return median
            elif len(nums2) % 2 == 0:
                median = (nums2[len(nums2)//2 - 1] + nums2[len(nums2) // 2])/2
                return median
        elif len(nums1) != 0 and len(nums2) == 0:
            if len(nums1) % 2 == 1:
                median = nums1[len(nums1) // 2]
                return median
            elif len(nums1) % 2 == 0:
                median = (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
                return median

    total_len = len(nums1) + len(nums2)
    # odd number of elements in the concatenated array
    if total_len % 2 == 1:
        left_part_len = (total_len + 1) // 2
        # nums1 being the shorter array
        if len(nums1) < left_part_len:
            nums1_lower_bound = 0
            nums1_upper_bound = len(nums1)
        # nums1 being the longer array
        else:
            # make sure the nums1 always end up being the shorter one between the two
            # swapping takes O(1)
            temp = nums1
            nums1 = nums2
            nums2 = temp
            nums1_lower_bound = 0
            nums1_upper_bound = len(nums1)

        # conduct binary search on the number of nums1 elements in the left part of the array:
        median = True
        while nums1_lower_bound <= nums1_upper_bound:
            nums1Count = (nums1_lower_bound + nums1_upper_bound) // 2
            nums2Count = left_part_len - nums1Count
            if nums1Count == 0:
                x = None
                x_dash = nums1Count
                y = nums2Count - 1
                y_dash = None
            elif nums1Count == len(nums1):
                x = nums1Count - 1
                x_dash = None
                y = nums2Count - 1
                y_dash = nums2Count
            else:
                x = nums1Count - 1
                x_dash = nums1Count
                y = nums2Count - 1
                y_dash = nums2Count

            median = checkMedian(nums1, nums2, x, x_dash, y, y_dash, median)
            if type(median) == float or type(median)==int:
                nums1_lower_bound=nums1_upper_bound+1
            else:
                if x != None and x_dash != None and y != None and y_dash != None:
                    # increase nums1's contribution
                    if nums1[x_dash] < nums2[y]:
                        nums1_lower_bound = nums1Count + 1
                    # decrease nums1's contribution
                    elif nums1[x] > nums2[y_dash]:
                        nums1_upper_bound = nums1Count - 1
                elif x == None and x_dash != None and y != None and y_dash == None:
                    # increase nums1's contribution
                    if nums1[x_dash] < nums2[y]:
                        nums1_lower_bound = nums1Count + 1
                elif x != None and x_dash == None and y != None and y_dash != None:
                    # decrease nums1's contribution
                    if nums1[x] > nums2[y_dash]:
                        nums1_upper_bound = nums1Count - 1

            # elif nums1[nums1Count-1] > nums2[nums2Count]:
            #     nums1_upper_bound = nums1Count - 1
            # elif nums1[nums1Count] < nums2[nums1Count-1]:
            #     nums1_lower_bound = nums1Count + 1
        return median
    # even number of elements in the concatenated array
    else:
        left_part_len = (total_len) // 2
        # nums1 being the shorter array
        if len(nums1) < left_part_len:
            nums1_lower_bound = 0
            nums1_upper_bound = len(nums1)
        # equal len nums1 and nums2
        elif len(nums1) == left_part_len:
            nums1_lower_bound = 0
            nums1_upper_bound = left_part_len
        # nums1 being the longer array
        else:
            # make sure the nums1 always end up being the shorter one between the two
            # swapping takes O(1)
            temp = nums1
            nums1 = nums2
            nums2 = temp
            nums1_lower_bound = 0
            nums1_upper_bound = len(nums1)

        # conduct binary search on the number of nums1 elements in the left part of the array:
        median = True
        while nums1_lower_bound <= nums1_upper_bound:
            nums1Count = (nums1_lower_bound + nums1_upper_bound) // 2
            nums2Count = left_part_len - nums1Count
            if nums1Count == 0:
                x = None
                x_dash = nums1Count
                if nums2Count < len(nums2):
                    y = nums2Count - 1
                    y_dash = nums2Count
                elif nums2Count == len(nums2):
                    y = nums2Count - 1
                    y_dash = None
            elif nums1Count == left_part_len:
                x = nums1Count - 1
                x_dash = None
                y = None
                y_dash = nums2Count
            elif nums1Count == len(nums1):
                x = nums1Count - 1
                x_dash = None
                y = nums2Count - 1
                y_dash = nums2Count
            else:
                x = nums1Count - 1
                x_dash = nums1Count
                y = nums2Count - 1
                y_dash = nums2Count

            median = checkMedian(nums1, nums2, x, x_dash, y, y_dash, median)
            if type(median) == float or type(median) == int:
                nums1_lower_bound=nums1_upper_bound+1
            else:
                if x != None and x_dash != None and y != None and y_dash != None:
                    # increase nums1's contribution
                    if nums1[x_dash] < nums2[y]:
                        nums1_lower_bound = nums1Count + 1
                    # decrease nums1's contribution
                    elif nums1[x] > nums2[y_dash]:
                        nums1_upper_bound = nums1Count - 1
                elif x == None and x_dash != None and y != None and y_dash == None:
                    # increase nums1's contribution
                    if nums1[x_dash] < nums2[y]:
                        nums1_lower_bound = nums1Count + 1
                elif x != None and x_dash == None and y != None and y_dash != None:
                    # decrease nums1's contribution
                    if nums1[x] > nums2[y_dash]:
                        nums1_upper_bound = nums1Count - 1
                elif x != None and x_dash == None and y == None and y_dash != None:
                    # decrease nums1's contribution
                    if nums1[x] > nums2[y_dash]:
                        nums1_upper_bound = nums1Count - 1
                elif x == None and x_dash != None and y != None and y_dash != None:
                    # increase nums1's contribution
                    if nums1[x_dash] < nums2[y]:
                        nums1_lower_bound = nums1Count + 1




            # elif nums1[nums1Count-1] > nums2[nums2Count]:
            #     nums1_upper_bound = nums1Count - 1
            # elif nums1[nums1Count] < nums2[nums1Count-1]:
            #     nums1_lower_bound = nums1Count + 1
        return median

print(sorted_median(nums1,nums2))

