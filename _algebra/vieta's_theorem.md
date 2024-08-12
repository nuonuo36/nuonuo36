---
title:  "Vieta's Theorem"
date: 2024-6-27 17:22:24 +0800
categories: quadratic
group: [quadratic]
---

## Theorem


Given $a_nx^n+a_{n-1}x^{n-1}+\dotsb+a_1x+a_0x=0$, let the roots be $r_1,r_2,\dotsc,r_n$.

# Proof 1

\begin{align*}
&a_nx^n+a_{n-1}x^{n-1}+\dotsb+a_1x+a_0x=0\\
&\Rightarrow a_n(x-r_1)(x-r_2)\dotsm(x-r_n) \\
&= a_nx^n+(-1)^1\cdot a_nx^{n-1}(r_1+r_2+\dotsb+r_n) \\
&+(-1)^2\cdot a_nx^{n-2}(r_1r_2+r_2r_3+\dotsb+r_{n-1}r_n) \\
&\vdots \\
&+(-1)^{n-1}\cdot a_nx(r_1r_2\dotsm r_{n-1} + r_2r_3\dotsm r_n) \\
&+(-1)^n\cdot a_n(r_1r_2\dotsm r_n) \\
\\
&a_{n-1}x^{n-1} = (-1)^1\cdot a_nx^{n-1}(r_1+r_2+\dotsb+r_n) \Rightarrow r_1+r_2+\dotsb+r_n=-\frac{a_{n-1}}{a_n} \\
&a_{n-2}x^{n-2} = (-1)^2\cdot a_nx^{n-2}(r_1r_2+r_2r_3+\dotsb+r_{n-1}r_n) \Rightarrow r_1r_2+r_2r_3+\dotsb+r_{n-1}r_n=\frac{a_{n-2}}{a_n} \\
\vdots& \\
&a_1x = (-1)^{n-1}\cdot a_nx(r_1r_2\dotsm r_{n-1} + r_2r_3\dotsm r_n) \Rightarrow r_1r_2\dotsm r_{n-1} + r_2r_3\dotsm r_n=(-1)^{n-1} \cdot\frac{a_1}{a_n} \\
&a_0 = (-1)^n \cdot a_n(r_1r_2\dotsm r_n) \Rightarrow r_1r_2\dotsm r_n = (-1)^n \cdot\frac{a_0}{a_n}
\end{align*}
