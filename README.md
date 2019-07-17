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
## Ongoing
1. With A_z = Pr[Alice chooses to send a Z basis], B_ = Pr[Bob Measures], P_k[Key round not used for stats]. We want to re express the parameters in terms of these parameters. 
2. Implement change in Code.
3. Consider the effects of changing these three parameters on the final key length.

##Notes
Table of what values we want to minimize and which we want to maximize. Observation, whether we want to maximize or minimize a statistic is independent of if Q_A = 2Q(1-Q) or Q=Q_A. Based on intuition I don't think this an actually interesting/surprising observation but more like we'd be concerned to some degree if it wasn't the case.

1. All statistics
| Statistic     | Add/Sub       |
| ------------- |:-------------:|
| p_{00}        | Add |
| p_{01}        | Add |
| p_{10}        | Sub |
| p_{11}        | Sub |
| p_{a0}        | Sub |
| p_{a1}        | Sub |
| p_{00a}       | Sub |
| p_{10a}       | Sub |
| p_{01a}       | Sub |
| p_{11a}       | Add |
| p_{a0a}       | Add |
| p_{a1a}       | Sub |
| p_{0R0}       | Sub |
| p_{0R1}       | Sub |
| p_{1R0}       | Sub |
| p_{1R1}       | Sub |

2. No reflection statistics
| Statistic     | Add/Sub       |
| ------------- |:-------------:|
| p_{00}        | Add |
| p_{01}        | Add |
| p_{10}        | Sub |
| p_{11}        | Sub |
| p_{a0}        | Sub |
| p_{a1}        | Sub |
| p_{00a}       | Sub |
| p_{10a}       | Sub |
| p_{01a}       | Sub |
| p_{11a}       | Add |
| p_{a0a}       | Add |
| p_{a1a}       | Sub |
| p_{0R0}       | Sub |
| p_{0R1}       | Add |
| p_{1R0}       | Add |
| p_{1R1}       | Sub |

3. No P_{?ZX} measurements
| Statistic     | Add/Sub       |
| ------------- |:-------------:|
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
| p_{0R1}       | Sub |
| p_{1R0}       | Sub |
| p_{1R1}       | Sub |

4. Neither
| Statistic     | Add/Sub       |
| ------------- |:-------------:|
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


### General questions
1. How many qubits are we considering?
	*  What are the affects of sending more or less qubits.
2. If our goal if to maximize the length of the final key, should Alice sends X basis qubits (more, same, less) than she sends Z basis qubits and likewise we would like to investigate biases how often Bob measures vs Reflect. 
3. Can we reduce the complexity of this problem via some actual algorithm that isn't 'sample everything'.
