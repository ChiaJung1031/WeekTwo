def maxProduct(nums):
    N = len(nums)
    for i in range(N-1):
     for j in range(N-i-1):
      if nums[j]>nums[j+1]:
       temp = nums[j]
       nums[j] = nums[j+1]
       nums[j+1] = temp
    
    if nums[0] <0 and nums[1]<0:
        first=nums[0]*nums[1]
        last=nums[N-1]*nums[N-2]
        if first > last:
            print(first)
        else:
            print(last)
    else:  
     max1=nums[N-1]
     max2=nums[N-2]
     maxnum= max1 * max2
     print(maxnum)

maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值