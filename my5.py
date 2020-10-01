def removeDuplicates(nums):
        print(type(nums))
        z=len(nums)
        for i in range(1,z):
            a=nums[0:i-1]+nums[i+1:]
            print(a)
            if nums[i] in a:
                nums.remove(nums[i])
        print(nums)
        return

removeDuplicates([1,2,2,4])

       
