"""
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.
"""

# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: 'Optional[Node]') -> 'Optional[Node]':
    
    # check if there's content in the list
    if not head:
        return head

    # create a pseudo node to act as the previous for the original list
    pseudo = Node(None, None, head, None)
    flatten_dfs(pseudo, head)

    # set the pseudo's next to null (detatch psudo from original linked list)
    pseudo.next.prev = None

def flatten_dfs(parent, child): # prev is the parent node, curr is the child node

    # check if there's a child node
    if not child:
        return parent

    # set the child's prev to the parent and the parent's next to the child
    child.prev = parent
    parent.next = child 

    # get a temporary child
    tempNext = child.next
    tail = flatten_dfs(child, child.child)
    child.child = None
    return flatten_dfs(tail, tempNext)


    