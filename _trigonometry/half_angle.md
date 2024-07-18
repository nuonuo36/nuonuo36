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

## Proof 1 (***for cosine and sine***)
Use [**Double Angle Formula**](../double_angle)

For half angle formula of **sine**, use double angle formula of **cosine**

$$
\begin{align*}
\text{substitue } 2\beta = \alpha  \\
\cos 2\alpha &= 1- 2\sin^2\beta   \\
\sin^2\beta &= \frac{1- \cos 2\beta}{2}  \hspace{1cm} \text{move terms}\\
\sin^2\frac{\alpha}{2} &= \frac{1- \cos \alpha}{2} \hspace{1cm} \text{substitue back} \\
\tag{1}\sin\frac{\alpha}{2} &= \pm\sqrt{\frac{1- \cos \alpha}{2}}
\end{align*}
$$

***WHY IS IT ADD AND MINUS SQRT***
For half angle formula of **cosine**, also use double angle formula of **cosine**

$$
\begin{align*}
\text{substitue } 2\beta = \alpha  \\
\cos 2\beta &= 2\cos^2\beta - 1 \\ 
\cos^2\beta &= \frac{1+\cos 2\beta}{2}  \hspace{1cm} \text{move terms}\\
\cos^2\frac{\alpha}{2} &= \frac{1+ \cos \alpha}{2} \hspace{1cm} \text{substitue back} \\
\tag{2}\cos\frac{\alpha}{2} &= \pm\sqrt{\frac{1+ \cos \alpha}{2}}
\end{align*}
$$

## Proof 2 (***for tangent***)
Use $$ \tan \beta = \frac{\sin \beta}{\cos \beta} $$

<!-- ### Step 1  -->

$$
\begin{align*}
\tan \frac{\alpha}{2} &= \frac{\sin \frac{\alpha}{2}}{\cos \frac{\alpha}{2}} \\
&= \frac{\pm\sqrt{\frac{1- \cos \alpha}{2}}}{\pm\sqrt{\frac{1+ \cos \alpha}{2}}}\hspace{1cm}\text{substitue both sine and cosine}\\
\tag{3} &= \pm\sqrt{\frac{1- \cos \alpha}{1+ \cos \alpha}} 
\end{align*}
$$

***WHY IS It PLUS MINUS***
<!-- \notag &= \frac{\pm\sqrt{\frac{1- \cos \alpha}{2}}}{\pm\sqrt{\frac{1+ \cos \alpha}{2}}} \hspace{1cm}\text{substitue cosine only}\\
\tag{4} &= \pm\sqrt{\frac{1- \cos \alpha}{1+ \cos \alpha}}
\notag &= \frac{\pm\sqrt{\frac{1- \cos \alpha}{2}}}{\pm\sqrt{\frac{1+ \cos \alpha}{2}}} \hspace{1cm}\text{substitue sine only}\\
\tag{5} &= \pm\sqrt{\frac{1- \cos \alpha}{1+ \cos \alpha}}
\end{align} -->