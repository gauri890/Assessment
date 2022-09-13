Problem statement :
Your company iRobot has created a new robot which can follow instructions

Solution :
Time complexity - O(n)
Space complexity - O(1)

Test case 1
Input - MSMEMWMN
Output - (1,0,N)

Test case 2 
Input - MSMMEMM 
Output - ( 3,3,E )

Test case 3
Input - WEMMSMNM
Output - ( 0,3,N )

Algorithm:
1. check command entered by user is valid, if not raise error
2. Traverse in command string if instructions is same as current direction 
3. if command String is 'M' then do not change current_direction
4. if command string is in ['N','S','E','W'] which is not same as current        direction change current direction and move forward in that direction



