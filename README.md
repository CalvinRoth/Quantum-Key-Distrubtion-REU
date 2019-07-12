# finiteKeyAnalysis
This is the code I developed for analyzing the Boyer SQKD protocol as part of my REU. This is a short description that I plan on adding to later

# What I have done so Far
1. I started by considering 2 parallel sets of 4 cases. These four cases are based on what statistics we do/don't have for estimating the key rate. The four cases are
*  All statistics are avaliable to us
*  We don't have mismatch reflection statistics
*  We don't have statistics of the form P_{?ZX} Where ? is anything, Z means a Z basis measurement and X means an X basis measurement
* Item 1d We don't have either of these statistics
2. Read paper about finite key in BB84 [Paper](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.100.200501)
3. Omar and I posed the hypothesis: If we have some uncertainity about the values of various parameters, e.g. we know P_{0R0} pm 0.25, the optimal noise occours on the boundary. That is with P_{0R0}+0.25 or P_{0R0}-0.25 procudes the optimal result
4. In hopes of solving this question, I numerically analyzed how adding a different error rate to parameters affected the optimal noise levels found. This will always be helpful later when we want to ask which statistics does it benefit us to be most sure about. 
5. Updated code so that parameters that we know should sum to 1 in reality do in the code. For Instance if P_{00}=0.25 then P_{01}=0.75. This gave higher key rates overall.
6. Adding an option for error in the Q_a level as well. 
7. Called 
