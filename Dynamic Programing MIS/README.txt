This folder has code for a dynamic programing assignment written in python for an algorithims class.

The sylabuss is bellow.

CS 532-001, Algorithms, Fall 2019
HW5 - DP (part 1: simple)

HWs 5-7 are all on DPs.

Due Monday Oct 28, 11:59pm.
No late submission will be accepted.

Need to submit report.txt, mis.py, bsts.py, bitstrings.py.
mis.py will be graded for correctness (1%).

To submit:
flip $ /nfs/farm/classes/eecs/fall2019/cs325-001/submit hw5 report.txt {mis,bsts,bitstrings}.py
(You can submit each file separately, or submit them together.)

To see your best results so far:
flip $ /nfs/farm/classes/eecs/fall2019/cs325-001/query hw5


Textbooks for References:
[1] CLRS Ch. 15
[2] KT Ch. 6
    or Ch. 5 in a previous version:
    http://cs.furman.edu/~chealy/cs361/kleinbergbook.pdf   

Hint: Among the three coding questions, p3 is the easiest, and p1 is similar to p3.
      You'll realize that both are very similar to p0 (Fibonacci).
      p2 is slightly different from these, but still very easy.

0. (Optional) Is Fibonacci REALLY O(n)?
   Hint: the value of f(n) itself grows exponentially.	    

1. [WILL BE GRADED]
   Maximum Weighted Independent Set 

   [HINT] independent set is a set where no two numbers are neighbors in the original list.
   	  see also https://en.wikipedia.org/wiki/Independent_set_(graph_theory)

   input:  a list of numbers (could be negative)
   output: a pair of the max sum and the list of numbers chosen

   >>> max_wis([7,8,5])
   (12, [7,5])

   >>> max_wis([-1,8,10])
   (10, [10])

   >>> max_wis([])
   (0, [])

   [HINT] if all numbers are negative, the optimal solution is 0,
          since [] is an independent set according to the definition above.

   >>> max_wis([-5, -1, -4])
   (0, [])

   Q: What's the complexity?
   
   Include both top-down (max_wis()) and bottom-up (max_wis2()) solutions, 
   and make sure they produce exact same results. 
   We'll only grade the top-down version.

   Tie-breaking: any best solution is considered correct.

   Filename: mis.py

   [HINT] you can also use the naive O(2^n) exhaustive search method to verify your answer.
   

2. Number of n-node BSTs

   input: n
   output: number of n-node BSTs

   >>> bsts(2)
   2
   >>> bsts(3)
   5
   >>> bsts(5)
   42

   [HINT] There are two 2-node BSTs:
      2    1
     /      \
    1        2
   Note that all other 2-node BSTs are *isomorphic* to either one.
      
   Qa: What's the complexity of this DP?
   
   Qb: What's the name of this famous number series?

   Feel free to use any implementation style.
   
   Filename: bsts.py

3. Number of bit strings of length n that has

   1) no two consecutive 0s.
   2) two consecutive 0s.
   
   >>> num_no(3)
   5
   >>> num_yes(3)
   3

   [HINT] There are three 3-bit 0/1-strings that have two consecutive 0s.
            001  100  000
          The other five 3-bit 0/1-strings have no two consecutive 0s:
	    010  011  101  110  111

   Feel free to choose any implementation style.

   Filename: bitstrings.py

   [HINT] Like problem 1, you can also use the O(2^n) exhaustive search method to verify your answer.


Debriefing (required!): --------------------------

0. What's your name?
1. Approximately how many hours did you spend on this assignment?
2. Would you rate it as easy, moderate, or difficult?
3. Did you work on it mostly alone, or mostly with other people?
4. How deeply do you feel you understand the material it covers (0%-100%)? 
5. Which part(s) of the course you like the most so far?
6. Which part(s) of the course you dislike the most so far?

This section is intended to help us calibrate the homework assignments. 
Your answers to this section will *not* affect your grade; however, skipping it
will certainly do.
