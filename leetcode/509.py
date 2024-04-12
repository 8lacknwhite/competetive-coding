class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        first=0
        second=1
        new_number=second
        if n==0:
            return 0
        else:
            for i in range(n-1):
                new_number = first+second
                first,second=second,new_number
            return new_number      