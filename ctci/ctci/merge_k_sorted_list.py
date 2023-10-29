import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        smallestList = []
        dummy = sortedList = ListNode(0,None)
        for arrayIdx in range(len(lists)):
            if lists[arrayIdx] is not None:
                node = lists[arrayIdx]
                smallestList.append((node.val,arrayIdx))
            
        heapq.heapify(smallestList)
        
        while smallestList:
            val,arrayIdx=heapq.heappop(smallestList)
            sortedList.next = ListNode(val,None)
            sortedList=sortedList.next
            
            node = lists[arrayIdx]
            node = node.next
            lists[arrayIdx] = node
            if not node:
                continue
            heapq.heappush(smallestList,(node.val,arrayIdx))
        return dummy.next