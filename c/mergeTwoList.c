/*************************************************************************
	> File Name:		mergeTwoList.c
	> Author:			ty-l6
	> Mail:				liuty196888@gmail.com
	> Created Time:		2017-08-17 Thu 23:47
 ************************************************************************/

#include<stdio.h>

/*! \struct ListNode
 *  \brief represent node in list
 *
 *  Detailed description
 */
struct ListNode {
	int val; /*!< val of this node */
	struct ListNode *next;
}ListNode;
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
	if (l1 == NULL) return l2;
	if (l2 == NULL) return l1;
	struct ListNode *head, *prev;
	if (l1->val >= l2->val){
		head = l2;
		l2 = l2->next;
	}else{
		head = l1;
		l1 = l1->next;
	}
	prev = head;
	while (l1 && l2){
		if (l1->val < l2->val){
			prev->next = l1;
			prev = l1;
			l1 = l1->next;
		}else{
			prev->next = l2;
			prev = l2;
			l2 = l2->next;
		}
	}
	if (l1) prev->next = l1;
	if (l2) prev->next = l2;
	return head;
}
void init(struct ListNode* l1, struct ListNode* l2)
{
	
}
