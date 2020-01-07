# Introductory-Programming-with-Python
## Exercise 1 
1. Function f(p, n) which takes as input an integer p > 1, a numeral n made up of k digits (n = ak−1ak−2...a0) and computes f(p, n) which is each digit power p.
2. Function g(p) which takes as input an integer p > 1 and returns a list of p + 5 elements, the element at index i being computed as i/10^(i−1).
3. Function h(p, L) which takes as input an integer p > 1, a list L and returns a list of boolean values with the same length as L and such that the element at index i is True if L[i] < 1/9^p . Test this function for some values of p and comment.
4. Create a list of 20 elements, the element at index i being computed as i × 9^3.
5. Write a function loop(p, n) which returns the list L of numerals forming the loop obtained while
computing successive images f(n), f^2(n), f^3(n), . . ..
## Exercise 2
List of test scores, produce a list associating each score with a rank (starting with 1 for the highest
score). Note that equal scores should have the same rank. For example, the input list [32, 75, 80, 50, 75,
32, 40] should produce the list of rankings [5,2,1,3,2,5,4].
## Exercise 3
Use a for loop to calculate π from the first 20 terms of the Madhava series.
## Exercise 4
Program which, given an list of integers, l1, calculates a list of the same length, l2 , in which l2 [i]
is the product of all the integers in l1 except l1 [i]. So, for example, if l1 = [4,1,3] , then l2 is [3, 12, 4].
## Exercise 5
Hero’s method for calculating the square root of a number, S, is as follows: starting with an initial guess, x0
, the sequence of numbers xn+1 = 1/2 (xn + S/xn) are successively better approximations to √S. Implement this algorithm to estimate the square root of 2117519.73 and compare with the “exact” answer provided by the math.sqrt method. For the purpose of this exercise, start with an initial guess, x0 = 2000.
## Exercise 6
The Fibonacci numbers are a sequence Fn of integers in which every number after the first two, 0 and
1 is the sum of the two preceding numbers. More formally, they are defined by the recurrence relation
Fn = Fn−1 + Fn−2, n ≥ 2 with the base values F0 = 0 and F1 = 1.
Program called fibonacci which inputs a number n and computes its fibonacci sequence.
