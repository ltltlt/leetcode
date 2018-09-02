package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

// partition list
// one loop is enough
func partition(head *ListNode, x int) *ListNode {
	var lhead, ltail, rhead, rtail *ListNode
	var cur *ListNode
	for cur = head; cur != nil; cur = cur.Next {
		if cur.Val >= x {
			if rtail != nil {
				rtail.Next = cur
			}
			rtail = cur
			if rhead == nil {
				rhead = cur
			}
			if ltail != nil {
				ltail.Next = cur.Next
			}
		} else {
			if ltail != nil {
				ltail.Next = cur
			}
			ltail = cur
			if lhead == nil {
				lhead = cur
			}
			if rtail != nil {
				rtail.Next = cur.Next
			}
		}
	}
	if lhead == nil {
		head = rhead
	} else {
		ltail.Next = rhead
		head = lhead
	}
	return head
}

func main() {
	l := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 4,
			Next: &ListNode{
				Val: 3,
				Next: &ListNode{
					Val: 2,
					Next: &ListNode{
						Val: 5,
						Next: &ListNode{
							Val: 2,
						},
					},
				},
			},
		},
	}
	l = partition(l, 3)
	for cur := l; cur != nil; cur = cur.Next {
		fmt.Println(cur.Val)
	}
}
