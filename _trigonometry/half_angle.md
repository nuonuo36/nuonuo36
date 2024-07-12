---
title:  "Half Angle Theorem"
date: 2024-6-27 17:22:24 +0800
categories: 
---

## Theorem 

$$
\begin{align}
\sin(\frac{\alpha}{2}) &= \pm \sqrt{\frac{1-\cos\alpha}{2}}\\

\cos(\frac{\alpha}{2}) &= \pm \sqrt{\frac{1+\cos\alpha}{2}}\\

\tan(\frac{\alpha}{2}) &= \pm \sqrt{\frac{1-\cos\alpha}{1+\cos\alpha}} \\
&= \frac{1-\cos\alpha}{\sin\alpha} \\
&= \frac{\sin\alpha} {1+\cos\alpha}\\
\end{align}
$$

## Proof 1

### Step 1
Use [**Double Angle Formula**](../double_angle)

For half angle formula of **sine**, use double angle formula of **cosine**

$$
\begin{align}
\notag \text{substitue } 2\beta = \alpha  \\
\notag \newline
\notag  2\sin^2\beta &= 1- \cos 2\beta  \\
\notag \sin^2\beta &= \frac{1- \cos 2\beta}{2}  \hspace{1cm} \text{move terms}\\
\notag \sin^2\frac{\alpha}{2} &= \frac{1- \cos \alpha}{2} \hspace{1cm} \text{substitue back} \\
\sin\frac{\alpha}{2} &= \pm\sqrt{\frac{1- \cos \alpha}{2}}
\end{align}

$$
