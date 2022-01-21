#https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        
        else:
            temp = self.reverseList(head.next)
            
            if(temp != None):
                temp_2 = temp
                while(temp.next != None):
                    temp = temp.next
                
                head.next = temp.next
                temp.next = head
            
            return temp_2
