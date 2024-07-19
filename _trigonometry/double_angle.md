---
title:  "Double Angle Theorem"
date: 2024-6-27 17:22:24 +0800
categories:
toc_sticky: true
group: [calculation]

---
## Theorem 

$$
\begin{align}
\sin 2\alpha &= 2\sin\alpha\cos\alpha \\

\cos 2\alpha &= \cos^2\alpha-\sin^2\alpha \\
&= 2\cos^2\alpha - 1 \\ 
&= 1 - 2\sin^2\alpha\\

\tan 2\alpha &= \frac{2\tan\alpha}{1-\tan^2\alpha}\\
\end{align}
$$

## Proof 1

### Step 1
Use [**Angle Addition Formula**](../angle_addition)

$$
\begin{align*}
\sin(\alpha + \alpha) &= \sin\alpha\cos\alpha + \sin\alpha\cos\alpha \\
\tag{1}\sin2\alpha &= 2\sin\alpha\cos\alpha \\

\\
\cos(\alpha + \alpha) &= \cos\alpha\cos\alpha - \sin\alpha\sin\alpha \\
\tag{2}\cos2\alpha &= \cos^2\alpha - \sin^2\alpha \\

\\
\tan(\alpha+\alpha) &= \frac{\tan\alpha + \tan\alpha}{1-\tan\alpha\tan\alpha} \\
\tag{5}\tan 2\alpha &= \frac{2\tan\alpha}{1-\tan^2\alpha}\\
\end{align*}
\\
$$

### Step 2 (for cosine only)
Use [**Pythagorean Identity**](../pythogorean_identity)

$$
\begin{align*}
\cos2\alpha &= \cos^2\alpha - (1-\cos^2\alpha) \\
\tag{3}&= 2\cos^2\alpha - 1 \\ 
\\
\cos2\alpha &= (1 -\sin^2\alpha) - \sin^2\alpha \\
\tag{4}&= 1 - 2\sin^2\alpha\\
\end{align*}
$$

