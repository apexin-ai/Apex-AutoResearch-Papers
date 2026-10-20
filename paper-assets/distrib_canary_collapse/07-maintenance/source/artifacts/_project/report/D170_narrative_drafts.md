# D170 Narrative Upgrade Drafts — Phase Diagram (α × T)

## Abstract 插入候选（1-2 句，插入在 detection boundary 公式之后）

### 选项 A（强调 T=5 blind zone）
> A phase diagram in contamination level and observation length reveals that at $T{=}5$, no contamination level produces detectable Granger-causal signal (0/8 across all $\alpha$), while extending to $T{=}20$ lowers the detection boundary from $\alpha_c{=}0.49$ to $\alpha_c{=}0.25$.

### 选项 B（强调整体 landscape 结构）
> Mapping the detection landscape across both $\alpha$ and $T$ reveals a structured phase diagram: a complete blind zone at $T{=}5$ (0/8 at all contamination levels), a synchronous dip persisting across $T$, and a detection boundary that traces a power-law contour through the $\alpha$--$T$ plane.

---

## Introduction C1 扩展候选（在现有 detection boundary 描述后追加）

### 草稿
> The phase diagram extends from one-dimensional dose-response to a two-dimensional detection landscape: at $T{=}5$, even $\alpha{=}0.75$ produces zero Granger-significant pairs, consistent with the theoretical prediction $\alpha_c(5) \geq 1.0$ from Proposition~\ref{prop:phase-boundary}; extending to $T{=}20$ lowers the boundary to $\alpha_c{=}0.25$, with the synchronous dip at $\alpha{=}0.60$ persisting across observation lengths ($p{=}0.064$ at $T{=}20$).

---

## Results 新段落：T=5 全暗行（§5.1 Sharp Detection Onset 末尾或 §5.4 T=20 之后）

### 草稿
> \paragraph{Detection blind zone at short observation length.}
> At $T{=}5$ (6 data points per series), PermG finds 0/8 Granger-significant pairs at every tested contamination level ($\alpha \in \{0.45, 0.50, 0.60, 0.75\}$), including conditions that yield reliable detection (6--8/8) at $T{=}10$ and $T{=}20$.
> This complete detection failure is quantitatively predicted by the phase boundary model: $\alpha_c(5) = 0.193 + 75.68 \cdot 5^{-2.41} \geq 1.0$, placing the detection threshold above any realizable contamination level.
> The $T{=}5$ blind zone demonstrates that observation length is not merely a power consideration but a hard constraint: below a critical $T$, no amount of contamination produces a statistically detectable causal signal, regardless of effect size.
> Combined with the $T{=}10$ and $T{=}20$ results, the phase diagram (Figure~\ref{fig:phase_diagram}) reveals the full two-dimensional detection landscape, where the boundary $\alpha_c(T)$ separates detectable from undetectable regions with a power-law contour.

---

## 备注

- T=5 数据来源：需确认 exp_id（D170 实验）
- "0/8 at all α" 包含 α=0.45/0.50/0.60/0.75，但 α<0.45 未测试
- 段落假设 T=5 结果与理论预测一致（α_c≥1.0）；如果实际有检出需修改
- Figure ref 使用 fig_phase_diagram 占位，需与 writing_plan 对齐
- 数字精度：α_c(5)=0.193+75.68×5^{-2.41}=0.193+75.68×0.01075≈1.01，确实≥1.0 ✅
