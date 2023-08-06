# 16. **Palindrome Linked List**: Given a singly linked list, determine if it is a palindrome.
#     - *Input*: [1,2,2,1]
#     - *Output*: "True"


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    if not head or not head.next:
        return True

    # Find the middle of the list
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the list
    second_half_head = reverse_list(slow.next)

    # Compare the first half with the reversed second half
    first_half = head
    second_half = second_half_head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


# Test the function
# Example linked list: 1 -> 2 -> 2 -> 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

result = is_palindrome(head)
print(result)
