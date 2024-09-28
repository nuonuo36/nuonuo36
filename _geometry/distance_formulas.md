---
title:  "Distance Formulas"
date: 2024-6-26 17:22:24 +0800
categories: euclidean_plane
group: [euclidean_plane]
layout: layout_proofs
includes: 
- \usepackage{tikz}
- \usepackage{pgfplots}
---

## Two Points


$$
\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}
$$

## Proof
Use **Pythagorean Theory**
Let Point A be ($x_1, y_1$), and Point B be ($x_2, y_2$)

Draw a right triangle

<p>
<script src="https://i.upmath.me/latex.js"></script>
$$
\begin{tikzpicture}
\usetikzlibrary {angles}
\draw (-2,0) -- (2,0);
\filldraw [gray] (0,0) circle (2pt);
\draw (-2,-2) .. controls (0,0) .. (2,-2);
\draw (-2,2) .. controls (-1,0) and (1,0) .. (2,2);
\end{tikzpicture}
$$
</p>

## One Point One Line

$$
\frac{|ax+by+c|}{\sqrt{a^2+b^2}}
$$


## Two Parallel Lines

$$
\frac{|c_1-c_2|}{\sqrt{a^2+b^2}}
$$

