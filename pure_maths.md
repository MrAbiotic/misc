# Probability of getting 8 digits without repetions
Note: In the given task, the leading digit is never 0, as that would make the number 7 digits.

## The process
There are eight spots to fill with numbers, which can be expressed as:

9 * 10 * 10 * 10 * 10 * 10 * 10 * 10
= 9 * 10^7
That means there are 90 millions different numbers you can express with the given restraints.


For the number of unique digits only, there is a pool of 10 digits, where the first digit has 9 possibilities.
Therefore the last 7 digits are expressed as nice factorial.
9 * 9! / 2!

Then we remember that to get percentage, we divide the part by the whole times 100:
(9 * 9! / 2!) / (9 * 10^7) * 100
= 1.8144

## The Answer
I have now used a mathematical proof, and a numerical method (1.80593).
Both yield roughly 1.81 percent, so I am pretty sure that is the answer, unless I have misunderstood the question.
