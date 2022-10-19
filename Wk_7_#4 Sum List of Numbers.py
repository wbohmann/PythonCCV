#4 Write and test a function for the following:
#sumList(nums) - nums is a list of numbers. Returns the sum of the numbers in the list..
 #nums is an argument that will loop through the list.  
 
def sumList(nums):
    listSum = 0 #sets the start for addition
    #create a loop through nums (the argument) adding num each time
    for num in nums:
        listSum += num
    return listSum #returns the amount each time
  
    
def main():
    num_list = [2,4,5,9] #a list of integers
    print("The sum of items is: ", sumList(num_list))
    
main()
