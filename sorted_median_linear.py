nums1 = [1, 3]
nums2 = [2]

nums1current = 0
nums2current = 0
result = []

while nums1current < len(nums1) or nums2current < len(nums2):
    if ((nums1current < len(nums1))==False and (nums2current < len(nums2))):
        result.append(nums2[nums2current])
        nums2current+=1

    elif ((nums2current < len(nums2))==False and (nums1current < len(nums1))):
        result.append(nums1[nums1current])
        nums1current+=1

    else:
        if nums1[nums1current] <= nums2[nums2current]:
            result.append(nums1[nums1current])
            nums1current+=1
        else:
            result.append(nums2[nums2current])
            nums2current+=1

if len(result) % 2 == 0:
    median = (result[len(result) // 2 - 1] + result[len(result) // 2]) / 2
else:
    median = result[len(result) // 2]
print(result)
print(median)