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
\usetikzlibrary {angles}
\tikz \draw (2,0) coordinate (A) -- (0,0) coordinate (B) -- (-1,-1) coordinate (C)
           pic [fill=black!50]                      {angle = A--B--C}
           pic [draw,->,red,thick,angle radius=1cm] {angle = C--B--A};
\end{tikzpicture}
$$
</p>

hi

<p>
<script src="https://i.upmath.me/latex.js"></script>
$$
\begin{tikzpicture}
\tikz \draw (2,0) coordinate (A) -- (0,0) coordinate (B) -- (-1,-1) coordinate (C)
pic ["$\alpha$", draw, ->] {angle};
\end{tikzpicture}
$$
</p>
