# finiteKeyAnalysis
This is the code I developed for analyzing the Boyer SQKD protocol as part of my REU. This is a short description that I plan on adding to later

## What I have done so Far
1. I started by considering 2 parallel sets of 4 cases. These four cases are based on what statistics we do/don't have for estimating the key rate. The four cases are
	*  All statistics are avaliable to us
	*  We don't have mismatch reflection statistics
	*  We don't have statistics of the form P_{?ZX} Where ? is anything, Z means a Z basis measurement and X means an X basis measurement
	*  We don't have either of these statistics
2. Read paper about finite key in BB84 [Paper](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.100.200501)
3. Omar and I posed the hypothesis: If we have some uncertainity about the values of various parameters, e.g. we know P_{0R0} pm 0.25, the optimal noise occours on the boundary. That is with P_{0R0}+0.25 or P_{0R0}-0.25 procudes the optimal result
4. In hopes of solving this question, I numerically analyzed how adding a different error rate to parameters affected the optimal noise levels found. This will always be helpful later when we want to ask which statistics does it benefit us to be most sure about. 
5. Updated code so that parameters that we know should sum to 1 in reality do in the code. For Instance if P_{00}=0.25 then P_{01}=0.75. This gave higher key rates overall.
6. Adding an option for error in the Q_a level as well. And generated corresponding resutls
7. Re organized code to be in multiple packages divided based on function and moved code to Git hub.
8. Determine all sets of dependent values. For instance P_{00} = 1 - P_{01} so we can sarfice the minimum bits in getting all of the statistics and what are expressions for them.
9. Found how to write the expected number of measurements of a statistic in terms of A_z, B_m, and P_k
10. Previous iteration bounded 
## Ongoing
1. Writing code that uses the E[m_ijk] in error estimation

##Notes

### Complexity of code

First, complexity in terms of what exactly? Presumably some variable representing how finely we sample over the different variables we sample over. Ignore for now If I say O(n^2) it's unclear what n is. 
Any ways. Setparms is O(1) it has no loops and just reassigns for varaibles and does basis arthimetic. 
Optim loops over Q, E[1], E[2], E[3] such that
	* 0<= Q <= 0.12
	* 0 <= E[1], E[2] <= Q(1-Q)
	* 0 <= E[3] <= Q^2
The runtime of these depends on how finely you sample these variables such that runtime = |Q|||E_1| |E_2| |E_3| which with the current step sizes of Q: 0.001 E_1:E_2:E_3: 0.01 this is about 7.5k iterations. Call this cost C. 

Finite Key samples 2 cases of Q = Q_A vs Q_a = 2Q(1-Q) x 4 cases of stats avaliable x 16 parameters to adjust ~= 128C. Real time run time is ~10 secs. We utlize previous experiments(data below) to not have to guess is p_ijk is in the range of p_ijk' \pm delta that the optimum occours at either + delta or -delta which we know which it is. 

### Table of max/min for each variable
Table of what values we want to minimize and which we want to maximize. Observation, whether we want to maximize or minimize a statistic is independent of if Q_A = 2Q(1-Q) or Q=Q_A. Based on intuition I don't think this an actually interesting/surprising observation but more like we'd be concerned to some degree if it wasn't the case. More importantly data analysis shows that the hypothesis the worst case noises occour on the boundaries of the allowable ranges of parameters is true. In english, I'm saying if P_{00} was 0.5 \pm 0.25, the worst case is either +0.25 or -0.25 which greatly simplifies optimizing. This data was gathered using a constant error rate intervals, like +0.25, +0.1, +0.01, 0, -0.01, etc. 

<summary> Click Here for tables </summary>
<a>
1. All statistics

| Statistic     | All Statistics     | No Reflection Statistics| No P_{?ZX}| Neither |
| ------------- |:-------------:|:-------------:|:------------:|:-----------:|
| p_{00}        | Add | Add | Sub | Sub |
| p_{01}        | Add | Add | Sub | Sub |
| p_{10}        | Sub | Sub | Sub | Sub |
| p_{11}        | Sub | Sub | Sub | Sub |
| p_{a0}        | Sub | Sub | Sub | Sub |
| p_{a1}        | Sub | Sub | Sub | Sub |
| p_{00a}       | Sub | Sub | Sub | Sub |
| p_{10a}       | Sub | Sub | Sub | Sub |
| p_{01a}       | Sub | Sub | Sub | Sub |
| p_{11a}       | Add | Add | Sub | Sub |
| p_{a0a}       | Add | Add | Sub | Sub |
| p_{a1a}       | Sub | Sub | Sub | Sub |
| p_{0R0}       | Sub | Sub | Sub | Sub |
| p_{0R1}       | Sub | Add | Sub | Add |
| p_{1R0}       | Sub | Add | Sub | Add |
| p_{1R1}       | Sub | Sub | Sub | Sub |

| p_{00}        | Sub |
| p_{01}        | Sub |
| p_{10}        | Sub |
| p_{11}        | Sub |
| p_{a0}        | Sub |
| p_{a1}        | Sub |
| p_{00a}       | Sub |
| p_{10a}       | Sub |
| p_{01a}       | Sub |
| p_{11a}       | Sub |
| p_{a0a}       | Sub |
| p_{a1a}       | Sub |
| p_{0R0}       | Sub |
| p_{0R1}       | Add |
| p_{1R0}       | Add |
| p_{1R1}       | Sub |

</a>


# Ongoing  Work

1. How do we calculate what delta_{ijk} is? I.e. how many what is the probability of observing state p_{ijk} for a parameter estimation step? 

2. What individual statistics do we need? This is relevant because we have some idea on what to say about groups so stats. 

	* What we have with A_z being Pr[ALice chooses Z], B_m = Pr[Bob measures], P_k = Pr[key is not used for stat gathering]
		a. P_{0Z} + P_{1Z} = B_m [A+z](1-P_k)
		b. P_{00Z} + P_{10Z} + P_{01Z} + P_{11Z} = B_m [A+z](1-P_k)
		c. P_{0RZ} + P_{1RZ} = A_Z (1-B_m)(1-P_k)
		d. P_{+0} + P_{+1} = (1-A_z) B_m (1-P_k)
		e. P_{+0+} + P_{+1+} + P_{+0-} + P_{+1-} = (1-A_z)B_m (1-P_k)
	* What are the statistics we actually need?
		a. For e000e021 + e001|e020
			pa0 x pa0a, p00 + p10, p00 x (p00a - 0.5), p10 x (p10a - 0.5),  pa0 ,p00 + p10
		b. for e110e131 + e111e130
        	(pa1 x pa1a), p01 + p11), p01 x (p01a - 0.5)), p11 x (p11a - 0.5), pa0, p00 + p10
        c. For cases where the reflection stats aren't 0
       		P0R0 x P0R1, P1R0 x P1R1

### General questions
1. Can we reduce the complexity of this problem via some actual algorithm that isn't 'sample everything'.

2. If I rewrote in C, we could consider doing some parallel computuation in parallel. There is a high degree of independent cases that makes this program other than the file output very easy in concept to parallelize. 
### Possible bugs
