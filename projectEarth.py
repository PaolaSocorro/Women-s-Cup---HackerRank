"""
Problem Statement

Project Earth, California's biggest environmental organization, is working to protect the planet Earth from global warming. Dr. Ritika is a scientist at Project Earth. She created a chemical called K29 which can increase the absorption rate of carbon dioxide by plants and help reduce global warming.

Unfortunately, K29 is not reacting the way it should. Dr. Ritika noticed that when K29 is used in plants, the reaction time is exactly T seconds. However, the chemical's reaction time changes as time passes, by following a specific pattern. It will change by 1 second every two hours, alternately increasing or decreasing every two hours. For the first two hours, the reaction time DECREASES by 1 second. During the next two hours, the reaction time INCREASES by 2 seconds. Then, for the next two hours, the reaction time DECREASES by 3 seconds. The reaction time follows this pattern by incremental seconds until the Nth hour.

Dr. Ritika needs the final reaction time in the Nth hour to correct K29. As her assistant, you must help Dr. Ritika correct the error so that she can save planet Earth. 
Given the value of N and an initial reaction time, T, find the final reaction time after N hours.

Input Format

The first, and only line, of input contains N and T separated by a space.

Constraints 
1≤ N ≤1016 
1≤ T ≤1016

Output Format

Print the final reaction time after N hours

Sample Input

Sample Input #00

5 3  
Sample Output#00

2
Explanation

N=5, T=3 

After the first hour, T decreases by 1 second so T=2  
After the second hour, T decreases by 1 second so T=1  
After the third hour, T increases by 2 seconds so T=3
After the fourth hour, T increases by 2 seconds so T=5
After the fifth hour, T decreases by 3 seconds so T=2
Sample Input #01

2 5
Sample Output#01

3
Explanation

N=2, T=5  

After the first hour, T decreases by 1 second so T=4  
After the second hour, T decreases by 1 second so T=3 

"""

x = raw_input().split()
N = int(x[0])
T = int(x[1])

if N % 4 == 0:
    delta = N/2
elif N % 4 ==1:
    delta = -1
    
elif N % 4 == 2:
    delta = (-N/2)-1
else:
    delta = 0
    
print int(T + delta)