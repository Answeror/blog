title: Hello
date: 2012-12-31
lang: en

**Hello**, from a *page*!

```python
def foo():
    pass
```

```markdown
$$ f(x) = \sum_{i=1}^N x^2 $$
```

$$ f(x) = \sum_{i=1}^N x^2 $$

```latex
\begin{equation}
\label{eq:beauty}
e^{i * \pi} + 1 = 0 
\end{equation}
```

\begin{equation}
\label{eq:beauty}
e^{i * \pi} + 1 = 0 
\end{equation}

test post commit hook

# Tikz

Normal Markdown...
Here is a tree:

\begin{tikzpicture}
  \draw[thick, level distance=3em] node{Root}
    child{ node{Child} }
    child{ node{Child} [sibling distance=3cm]
      child{ node{Grandchild} }
      child{ node{Grandchild} } };
\end{tikzpicture}

Using the *Lindenmayer* library:

\usetikzlibrary{lindenmayersystems}
\begin{tikzpicture}
  \draw[rotate=90]
    lindenmayer system[l-system={
      rule set={F -> FF-[-F+F]+[+F-F]},
      axiom=F, order=4,
      step=2pt, randomize step percent=25,
      angle=30, randomize angle percent=5}];
\end{tikzpicture}

More Markdown.

\begin{tikzpicture}[auto,>=stealth,swap,
  node/.style={draw,minimum width=24mm,text centered,minimum height=14mm}]
  \filldraw[fill=green!10,dashed,rounded corners=5mm]
    (-1,-8) -- (4,-8) -- (4,-11) -- (-1,-11) -- cycle;
  \filldraw[fill=blue!10,dashed,rounded corners=5mm]
    (6,-5) -- (13,-5) -- (13,-11) -- (6,-11) -- cycle;
  \node at (1,-10.5) {Foo};
  \node at (10.5,-10.5) {Bar};
  \node [node] (impl) at (1.5,-9) {Baz};
  \node [node] (lang) at (8,-6) {X};
  \node [node] (algo) at (11,-6) {Y};
  \node [node] (proto) at (9.5,-9) {Z};
  \draw[->] (lang) to node {} (proto);
  \draw[->] (algo) to node {} (proto);
  \draw[->,bend left] (impl) to node [swap,text centered]{Woo} (lang);
  \draw[->,bend right] (impl) to node [text centered]{Woo} (algo.south west);
\end{tikzpicture}

