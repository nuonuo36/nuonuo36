---
title:  "Triangle Area"
date: 2024-6-27 17:22:24 +0800
categories: 
group: [triangle]
---

<span style="color:green;font-weight:700;font-size:20px">
    markdown color font styles
</span>

## Base Height
### Proof

## Sine Formula

$$S_{\triangle ABC}= \frac{1}{2}ab\sin C $$

### Proof

* Use **Base Height** formula
* Notice how to express the alititude $$h$$ from B to b: $$\sin C = \frac{h}{a}$$, so $$ \sin C \cdot a = h $$

$$
\begin{align*}
S_{\triangle ABC} &= \frac{1}{2} \text{base} \cdot \text{height} \\ 
&=\frac{1}{2}b \cdot h \\
&= \frac{1}{2} b \cdot (\sin C \cdot a) \\
&=\frac{1}{2}ab\sin C \\
\end{align*}
$$

## Inscribed Circle (Angle Bisectors)
### Proof


<!-- ## Trapezoid
### Proof -->


## Centroid and Medians
### Proof


## Equilateral Triangle
Area of equilateral triangle = $$\frac{\sqrt{3}}{4}s^2$$
### Proof 1 
Use **Pythagorean Theorem** and **30-60-90** special triangle

Let the side-length of an equilateral triangle be $$s$$, so

altitude = a = $$\frac{\sqrt{3}}{2}s$$

base = b = $$s$$

area = A

$$
\begin{align*}
A &= \frac{a\cdot b}{2} \hspace{1px}\\
&=\frac{\sqrt{3}}{4}s^2 \\
\end{align*}
$$





## Heron's Formula
Area of triangle = $$\sqrt{s(s-a)(s-b)(s-c)}$$
### Proof

* Use [$$S_{\triangle ABC}= \frac{1}{2}ab\sin C $$](#sine-forumla)
* Use [**Law of Cosine**](trigonometry/law_of_cosine)
* Use [**Pythagorean Identities**](trigonometry/pythagorean_identities)
* Notice $$s-a = \frac{a+b+c}{2}-\frac{2a}{2} =  \frac{b+c-a}{2}$$


$$
\begin{align*}
&S_{\triangle ABC} = \frac{1}{2} ab\sin C \\
&= \frac{1}{2}ab \sqrt{1-\cos^2\theta} &\text{ Use Pythagorean Identity }\\
&= \frac{1}{2}ab \sqrt{1-(\frac{c^2 - a^2 - b^2}{2ab})^2} &\text{ Use Law of Cosine}\\
\end{align*}
$$


<details>
<summary>Simplify</summary>
$$
\begin{align*}
&= \frac{1}{2}ab \sqrt{\frac{(2ab)^2}{(2ab)^2}-(\frac{c^2 - a^2 - b^2}{2ab})^2} &\text{ Simplify}&\\
&= \frac{1}{2}ab \sqrt{\frac{(2ab)^2-(c^2 - a^2 - b)^2}{(2ab)^2}} &\text{ Simplify}&\\
&= \frac{1}{2}ab \frac{\sqrt{(2ab)^2-(c^2 - a^2 - b)^2}}{2ab} &\text{ Simplify}&\\
\end{align*}
$$
</details>

$$
\begin{align*}
&= \frac{1}{2}ab \frac{\sqrt{(2ab-c^2 + a^2 + b)(2ab+c^2 - a^2 - b)}}{2ab} &\text{ Use } a^2-b^2=(a-b)(a+b)\\
&= \frac{1}{2}ab \frac{\sqrt{((a+b)^2-c^2)(c^2-(a+b)^2)}}{2ab} &\text{ Use } (a+b)^2=a^2+2ab+b^2\\
&= \frac{1}{2}ab \frac{\sqrt{(a+b+c)(a+b-c)(c-a+b)(c+a-b)}}{2ab} &\text{ Use } a^2-b^2=(a-b)(a+b)\\
\end{align*}
$$

<details>
<summary>Simplify</summary>
$$
\begin{align*}
&= \frac{\sqrt{(a+b+c)(a+b-c)(c-a+b)(c+a-b)}}{4} \text{ Simplify}\\
&= \sqrt{\frac{(a+b+c)(a+b-c)(c-a+b)(c+a-b)}{16}} \text{ Simplify}\\
&= \sqrt{\frac{a+b+c}{2}\frac{a+b-c}{2}\frac{c-a+b}{2}\frac{c+a-b}{2}} \text{ Simplify}\\
\end{align*}
$$
</details>

$$
\begin{align*}
&= \sqrt{s(s-c)(s-a)(s-b)} \text{ Use *UHDWLIHDIELUSd*}\\
\end{align*}
$$

***Note $$a,b,c$$ are the sidelengths of a triangle, and $$s=\frac{a+b+c}{2}$$, the semi perimeter***

## Shoelace Theorem 
