---
title:  "Binomial Theorem"
date: 2024-6-27 17:22:24 +0800
categories: powers
group: [powers]
---

# Theorem

$$
(a+b)^n=\sum^{n}_{k=0}{n \choose k}a^{n-k}b^k
$$

# Proof 1

For each term in the summation, we are picking $k$ of $n$ $(a+b)$ to be $b$, and the rest to be $a$. Thus, the degree of $b$ and $a$ are $k$ and $n-k$ respectively. The coefficient of each term is the number of ways to choose k from n, thus the coefficient is ${n \choose k}$. Putting them together, each term is ${n \choose k}a^{n-k}b^k$, thus

$$
(a+b)^n=\sum^{n}_{k=0}{n \choose k}a^{n-k}b^k
$$