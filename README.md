# Log functions by iteration method

In this program I'll aproximate the log-function by an iteration method. Every iteraion improves the result. 

> An iterative algorithm with fast convergence can be used to compute logarithms,
> inverse circular functions, or inverse hyperbolic functions according to the choice of initial
> conditions. Only rational operations and square roots are required. The method consists in
> adding an auxiliary recurrence relation to Borchardt's algorithm to speed the convergence.
>
> -- <cite>B. C. Carlsson: An Algorithm for Computing Logarithms nd Arctangents, MathComp. 26 (118), 1972 pp. 543-549.</cite>

It is based of computing the arithmetic and geometric mean of two values ai, gi:
- For a given value $x > 0$, initialize $a_0 = \frac{1+x}{2}$ , $g_0 = \sqrt{k}$,
- Iterate $a_{i+1} = \frac{a_i + g_i}{2}$ and $g_{i+1} = \sqrt{a_i+1g_i}$,
- Consider $\frac{x-1}{a_i}$ as an approximation to $ln(x)$.


