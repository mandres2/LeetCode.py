"""
881. Boats to Save People

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
"""

# Solution:
"""
Since we want to minimise the number of boats used, we must try to form pair of largest and smallest numbers to fit them into one boat if possible. Taking two smaller weight people and adding them to one boat might waste some precious space.
Now we can see that as 12 tries to form a pair. Logically being the largest number it should start from the smallest. So it goes to 1's, then 2 then 3 and so on to form a pair. Now one thing to note is that if 12 cannot form a pair with the smallest number(that is 1), then there is no point looking forward to 2, 3 ... as it is certain that numbers beyond 1 will be equal to or larger than 1 and will definitely exceed the boats rated capacity if it did with 1 in the first place.
Thus if the people[hi] cannot be seated with people[lo] in one boat then that means that people[hi] cannot form a pair with any of the remaining people, and we will thus stop looking for a partner for that person and give him a boat for him/her self.

STEPS:

Maintain 2 pointers lo and hi set to 0 and n-1 respectively.
Sort the array people.
Now traverse till lo <= hi.
If people[lo] + people[hi] <= target. That means they can form a pair and can sit in the same boat.
If not then the people[hi] that is the person with the higher weight is the problem and must be given his own boat as we observed above.
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo = 0
        hi = len(people)-1
        boats = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
                hi -= 1
            else:
                hi -= 1
            boats += 1
        return boats
