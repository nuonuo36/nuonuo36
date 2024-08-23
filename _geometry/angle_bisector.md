---
title: "Angle Bisector Theorem"
date: 2024-6-26 17:22:24 +0800
categories: triangle
group: [triangle]

includes: 
  - \usepackage{tikz}
  - \usepackage{pgfplots}
---

## Theorem

## Proof 



<p>
<script src="https://i.upmath.me/latex.js"></script>
$$
\begin{tikzpicture}
\draw[->] (-3,0) -- (-2,0) arc[radius=0.5cm,start angle=-180,end angle=0] (-1,0) -- (1,0) arc[radius=0.5cm,start angle=180,end angle=0] (2,0) -- (3,0);
\filldraw (-1.5,0) circle[radius=1mm];
\filldraw (1.5,0) circle[radius=1mm];
\end{tikzpicture}
$$
</p>



<p>
<script src="https://i.upmath.me/latex.js"></script>
$$
\begin{tikzpicture}
 % Draw the angle bisector AD
\coordinate[label=right:$D$] (D) at ($(B)!(A)!(C)$);
\draw[thick, color=red] (A) -- (D);
 % Label the sides 
\draw ($(B)!0.5!(C)$) node[above] {$c$};
\draw ($(A)!0.5!(C)$) node[above] {$b$};
\draw ($(A)!0.5!(B)$) node[below] {$a$};
 % Draw right angles
\draw [color=blue] ($(A)!0.6!(D)$) -- ++(-90:0.2) -- ++(180:0.2) -- ++(90:0.2);
% Mark the angle bisector
\node at (1,1.4) [above left] {\textcolor{red}{$\theta$}};
\node at (3,1.4) [above right] {\textcolor{red}{$\theta$}};
\end{tikzpicture}
\begin{tikzpicture}
% Define the vertices of the triangle
\coordinate [label=left:$A$] (A) at (0,0);
\coordinate [label=right:$B$] (B) at (4,0);
\coordinate [label=above:$C$] (C) at (2,3);
% Draw the sides of the triangle
\draw [thick] (A) -- (B) -- (C) -- cycle;
% Optional: Draw the labels on the sides
\node at (2,-0.3) {$c$};
\node at (0.7,1.7) {$b$};
\node at (3.2,1.7) {$a$};
\end{tikzpicture}
$$
</p>