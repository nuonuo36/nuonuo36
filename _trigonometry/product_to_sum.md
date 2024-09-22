---
title:  "Product to Sum"
date: 2024-6-27 17:22:24 +0800
categories: 
group: [calculation]
---

## Theorem

$$ 
\begin{align}
\sin\alpha+\sin\beta &= 2\sin(\frac{\alpha+\beta}{2})\cos(\frac{\alpha-\beta}{2}) \\
\sin\alpha-\sin\beta &= 2\cos(\frac{\alpha+\beta}{2})\sin(\frac{\alpha-\beta}{2}) \\ 
\cos\alpha+\cos\beta &= 2\cos(\frac{\alpha+\beta}{2})\cos(\frac{\alpha-\beta}{2}) \\
\cos\alpha-\cos\beta &= -2\sin(\frac{\alpha+\beta}{2})\sin(\frac{\alpha-\beta}{2}) \\
\tan\alpha+\tan\beta &= \frac{\sin(\alpha+\beta)}{\cos\alpha\cos\beta} \\
\tan\alpha-\tan\beta &= \frac{\sin(\alpha-\beta)}{\cos\alpha\cos\beta} \\
\end{align}

$$

# Proof

Express $\alpha$ as $x+y$
Express $\beta$ as $x-y$
Thus, $x$ is $\frac{\alpha+\beta}{2}$ and $y$ is $\frac{\alpha-\beta}{2}$

<details>
<summary>Show me why</summary>
$$
\begin{align*}
\alpha = x+y
\beta = x-y
\alpha+\beta = x+y+x-y \text{add the two equations}
x = \frac{\alpha+\beta}{2}
\alpha-\beta = x+y-x+y \text{minus the two equations}
y = \frac{\alpha-\beta}{2}
\end{align*}
$$
</details>

* Use [**Angle Addition Formula**](../angle_addition)

$$ 
\begin{align}
\sin\alpha+\sin\beta &= \sin(x+y)+\sin(x-y)
&= \sin(x)\cos(y)+\sin(y)\cos(x)+\sin(x)\cos(y)-\sin(y)\cos(x)
&= 2\sin(x)\cos(y)

\end{align}
$$
