# 2336. Smallest Number in Infinite Set

"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

Solution: Hashset and Heap
Algorithm
Initialize some variables:

isPresent, a hash set to store the removed numbers added again.
addedIntegers, a min-heap priority queue to store the minimum of all added numbers on the top.
currentInteger, an integer variable initialized to 1, used to denote the current minimum value number in the set of all positive numbers.
In the popSmallest() method:

If we have any element present in the min-heap addedIntegers, then the minimum number present in it is the answer. We remove it from the min-heap and the hash set isPresent.
Otherwise, the number denoted by currentInteger is our answer, and then we increment currentInteger by 1 which denotes we removed the previous number and moved to the next number in our set of all positive numbers.
In the end, we return answer.
In the addBack(num) method:

If the 'num' is already present in our set, then we do nothing and return. This is the case if currentInteger <= num or num is in isPresent.
Otherwise, we push it into min-heap addedIntegers and hash set isPresent.

Time-Complexity: O((m+n) * log n)
Space-Complexity: O(n)
"""
class SmallestInfiniteSet:
    def __init__(self):
        self.is_present: {int} = set()
        self.added_integers: [int] = []
        self.current_integer = 1

    def popSmallest(self) -> int:
        # If there are numbers in the min-heap, 
        # top element is lowest among all the available numbers.
        if len(self.added_integers):
            answer = heapq.heappop(self.added_integers)
            self.is_present.remove(answer)
        # Otherwise, the smallest number of large positive set 
        # denoted by 'current_integer' is the answer.
        else:
            answer = self.current_integer
            self.current_integer += 1
        return answer

    def addBack(self, num: int) -> None:
        if self.current_integer <= num or num in self.is_present:
            return
        # We push 'num' in the min-heap if it isn't already present.
        heapq.heappush(self.added_integers, num)
        self.is_present.add(num)
