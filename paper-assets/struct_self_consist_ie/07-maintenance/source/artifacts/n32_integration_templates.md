# N=32 Pretrained Integration Templates

> 准备好的模板，n32 回调后填数字即可。

## 共同项：Appendix Table 44 新增行

```latex
Few-NERD & Pretrained ($N{=}32$) & .XXX & $+$X.X & X.X & XX\% & .XXX \\
```

---

## 情况 A：Plateau（MV ~3.5-4.5pp）

### Appendix 文本（在 N=16 句后追加）
```latex
$N{=}32$ confirms the plateau (MV $\Delta{=}+X.X$\,pp), with capture rate declining further to $XX$\%.
```

### Discussion：不改（当前句已覆盖 "plateaus rather than scales"）

---

## 情况 B：增长（MV >5pp）

### Discussion:14 替代句
```latex
The MV advantage persists and continues scaling sub-linearly at $N{=}32$ ($+X.X$\,pp; Table~\ref{tab:pretrained_summary}), though capture rate decreases---oracle headroom expands ($11.2{\to}XX.X$\,pp) faster than MV gains, suggesting diminishing returns.
```

### Appendix 文本
```latex
At $N{=}32$, pretrained MV gains continue increasing ($+X.X$\,pp), though the rate of improvement decelerates (capture rate $XX$\% vs.\ $29$\% at $N{=}16$).
```

---

## 情况 C：下降（MV <3pp）

### Discussion:14 替代句
```latex
Pretrained MV gains peak at moderate sample sizes ($N{=}8$--$16$, ${\approx}+4$\,pp) before declining at $N{=}32$ ($+X.X$\,pp; Table~\ref{tab:pretrained_summary}), suggesting an optimal sampling budget exists even for pretrained models.
```

### Appendix 文本
```latex
At $N{=}32$, MV gains decrease to $+X.X$\,pp despite further degeneracy reduction ($X.X$\%), indicating that the voting aggregation ceiling tightens with increasing $N$.
```
