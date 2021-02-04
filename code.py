#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the removeDuplicates function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    if head is None or head.next is None:
        return head
   # 1 3 3  3 4 5 5
    l=list()
    temp=head
    prev=head
    while(temp):
        if (temp.data not in l):
            l.append(temp.data)
            prev=temp
            #temp=temp.next 
            
        else:  
            #print(prev.data) 
            if prev.next is not None:
                prev.next=prev.next.next 
                
            else:
                continue    
            
        temp=temp.next    
       # print('p',prev.data)   

                    
       
             
    
    
    return head

if __name__ == '__main__':