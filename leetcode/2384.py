import collections

# You are given a string num consisting of digits only.

# Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

# Notes:

# You do not need to use all the digits of num, but you must use at least one digit.
# The digits can be reordered.
 

# Example 1:

# Input: num = "444947137"
# Output: "7449447"
# Explanation: 
# Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
# It can be shown that "7449447" is the largest palindromic integer that can be formed.
# Example 2:

# Input: num = "00009"
# Output: "9"
# Explanation: 
# It can be shown that "9" is the largest palindromic integer that can be formed.
# Note that the integer returned should not contain leading zeroes.


class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        # high level build mapping 
        # organise string to form highest number - track first bit and then revert 
        # centre number can be a one off 
        
        # build a map/ hashmap to count how many times each number occurs in string 
                
                

        # centre element - keep track off, we dont need multiple values
        
        # return a string as input 